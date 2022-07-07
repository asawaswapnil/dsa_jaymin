from __future__ import annotations


import time
import threading
from enum import Enum
from typing import Dict, Deque, Callable, Optional
from collections import deque
from dataclasses import dataclass
from functools import wraps


def record(operation: KVStore.Operation) -> Callable:
    """
    A utility decorator `@record` that takes an operation type and records a hit in an asynchronous fashion.
    """
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(self: KVStore, *args, **kwargs):
            # The `append` and `popleft` operations on `collections.deque` are thread-safe
            # Reference: https://docs.python.org/3/library/collections.html#deque-objects
            # If they weren't, we could have used a reentrant lock `threading.RLock` for synchronized updates
            threading.Thread(target=self._hit_counter.record_hit, args=(operation,)).start()
            return fn(self, *args, **kwargs)
        return wrapper
    return decorator


class KVStore:
    """
    A toy implementation of an in-memory key-value store like Memcached or Redis.
    The KVStore has three methods:
    - get(key) => returns the value if the key exists in the store or returns `None`
    - put(key, value) => add a value for a given key in the store
    - qps_load(operation) => returns the QPS load of an operation (get/put) in past `duration_secs`
    """
    class Operation(Enum):
        GET = 0
        PUT = 1

    def __init__(self):
        self._store: Dict[str, int] = {}
        self._hit_counter = HitCounter(duration_secs=DURATION_SECS)

    @record(Operation.GET)
    def get(self, key: str) -> Optional[int]:
        return self._store.get(key)

    @record(Operation.PUT)
    def put(self, key: str, value: int) -> None:
        self._store[key] = value

    def qps_load(self, operation: KVStore.Operation) -> int:
        return self._hit_counter.get_qps(operation)


@dataclass
class TimeWindow:
    start_time: int
    end_time: int
    hits: int = 0


class HitCounter:
    """
    An implementation of a HitCounter that keeps track of number of requests for different methods of a key-value store
    in past `duration_secs` seconds. The key-value store being used here is `KVStore` which is a toy implementation of
    an in-memory key-value store like Memcached or Redis.

    It maintains fixed size buffers (`deque` or a doubly-ended queue) for all operations. The idea is to always keep
    the buffers in a valid state. Valid state here means there are no stale entries (hits for requests older than
    `duration_secs`). So every time we try to record a hit or compute QPS, we first update the buffers to be in a
    consistent/valid state.

    Runtime complexities:
    The `append` and `popleft` operations on `collections.deque` take amortized O(1) time. This means updating the
    buffers, recording a hit and computing QPS is all constant time since the buffers are of fixed size.
    The space complexity is also O(1) since at most there will be `duration_secs` time windows at a given time.
    """
    HEAD = 0
    TAIL = -1

    def __init__(self, duration_secs: int):
        self._duration: int = duration_secs
        self._buffers: Dict[KVStore.Operation, Deque[TimeWindow]] = {
            op: deque([], maxlen=self._duration) for op in KVStore.Operation
        }

    def record_hit(self, operation: KVStore.Operation) -> None:
        """
        Record a hit for the `operation`
        """
        current_time = HitCounter.get_current_time()
        queue = self._buffers[operation]
        self._update_queue(queue, current_time)

        if queue and queue[self.TAIL].end_time > current_time:
            queue[self.TAIL].hits += 1
        else:
            time_window = TimeWindow(start_time=current_time, end_time=current_time + 1, hits=1)
            queue.append(time_window)

    def get_qps(self, operation: KVStore.Operation) -> int:
        """
        Computes and returns QPS of an `operation`
        """
        current_time = HitCounter.get_current_time()
        queue = self._buffers[operation]
        self._update_queue(queue, current_time)

        if not queue:
            return 0

        total_hits = 0
        total_secs = current_time - queue[self.HEAD].start_time or 1
        for window in queue:
            total_hits += window.hits
        return total_hits // total_secs

    def _update_queue(self, queue: Deque[TimeWindow], current_time: int) -> None:
        """
        Ensures the queue is in valid state, wherein it doesn't hold request counts for any requests older than the
        specified duration
        """
        oldest_allowed_time = current_time - self._duration
        if queue and queue[self.TAIL].end_time <= oldest_allowed_time:
            queue.clear()  # All time windows in the queue are stale
            return

        # Start removing stale time windows from the left to right (oldest -> newest)
        while queue and queue[self.HEAD].end_time <= oldest_allowed_time:
            queue.popleft()

    @staticmethod
    def get_current_time() -> int:
        """
        Returns the integer value of an epoch timestamp for current time
        """
        return int(time.time())


if __name__ == '__main__':
    DURATION_SECS = 2

    kv_store = KVStore()
    kv_store.put("a", 1)
    kv_store.put("b", 2)
    kv_store.put("c", 3)
    kv_store.get("a")

    print(kv_store.qps_load(KVStore.Operation.PUT))  # should be 3
    print(kv_store.qps_load(KVStore.Operation.GET))  # should be 1

    time.sleep(DURATION_SECS)

    print(kv_store.qps_load(KVStore.Operation.PUT))  # should be 1
    print(kv_store.qps_load(KVStore.Operation.GET))  # should be 0, the QPS value is rounded down to the nearest integer

    kv_store.get("b")
    time.sleep(1)

    print(kv_store.qps_load(KVStore.Operation.PUT))  # should be 0
    print(kv_store.qps_load(KVStore.Operation.GET))  # should be 1
