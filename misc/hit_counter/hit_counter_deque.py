from __future__ import annotations

from threading import RLock
from collections import deque
from dataclasses import dataclass
from typing import Dict, Deque

from misc.hit_counter import KVStore, HitCounter


class HitCounterDeque(HitCounter):
    """
    A thread-safe implementation of HitCounter using Deque.

    It maintains fixed size buffers (`deque` or a doubly-ended queue) for all operations. The idea is to always keep
    the buffers in a valid state. Valid state here means there are no stale entries (hits for requests older than
    `duration_secs`). So every time we try to record a hit or compute QPS, we first update the buffers to be in a
    consistent/valid state.

    Runtime complexities:
    The `append` and `popleft` operations on `collections.deque` take amortized O(1) time. This means updating the
    buffers, recording a hit and computing QPS is all constant time since the buffers are of fixed size.
    The space complexity is also O(1) since at most there will be `duration_secs` time windows at a given time.
    """

    @dataclass
    class TimeWindow:
        start_time: int
        end_time: int
        hits: int = 0

    HEAD = 0
    TAIL = -1

    def __init__(self, duration_secs: int):
        self._duration: int = duration_secs
        self._buffers: Dict[KVStore.Operation, Deque[HitCounterDeque.TimeWindow]] = {
            op: deque([], maxlen=self._duration) for op in KVStore.Operation
        }
        self._locks: Dict[KVStore.Operation, RLock] = {
            op: RLock() for op in KVStore.Operation
        }

    def record_hit(self, operation: KVStore.Operation) -> None:
        """
        Record a hit for the `operation`
        """
        current_time = self.get_current_time_int()
        queue = self._buffers[operation]
        with self._locks[operation]:
            self._update_queue(queue, current_time)

            if queue and queue[self.TAIL].end_time > current_time:
                queue[self.TAIL].hits += 1
            else:
                time_window = HitCounterDeque.TimeWindow(start_time=current_time, end_time=current_time + 1, hits=1)
                queue.append(time_window)

    def get_qps(self, operation: KVStore.Operation) -> int:
        """
        Computes and returns QPS of an `operation`
        """
        current_time = self.get_current_time_int()
        queue = self._buffers[operation]
        with self._locks[operation]:
            self._update_queue(queue, current_time)

            if not queue:
                return 0

            total_hits = 0
            total_secs = current_time - queue[self.HEAD].start_time or 1
            for window in queue:
                total_hits += window.hits
            return total_hits // total_secs

    def _update_queue(self, queue: Deque[HitCounterDeque.TimeWindow], current_time: int) -> None:
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
