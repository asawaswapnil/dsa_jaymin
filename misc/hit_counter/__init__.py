from __future__ import annotations

import time
import threading
from enum import Enum
from functools import wraps
from typing import Dict, Callable, Optional, Type
from abc import ABC, abstractmethod


def record(operation: KVStore.Operation) -> Callable:
    """
    A utility decorator `@record` that takes an operation type and records a hit in an asynchronous fashion.
    """

    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(self: KVStore, *args, **kwargs):
            # Python is single-threaded due to GIL, so we don't really need explicit pessimistic locking for hit counters
            # But for illustrative purpose, the hit cuonters use reentrant locks `threading.RLock` for synchronized operations
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

    def __init__(self, hit_counter_impl: Type[HitCounter], hit_tracking_duration: int):
        self._store: Dict[str, int] = {}
        self._hit_counter: HitCounter = hit_counter_impl(duration_secs=hit_tracking_duration)

    @record(Operation.GET)
    def get(self, key: str) -> Optional[int]:
        return self._store.get(key)

    @record(Operation.PUT)
    def put(self, key: str, value: int) -> None:
        self._store[key] = value

    def qps_load(self, operation: KVStore.Operation) -> int:
        return self._hit_counter.get_qps(operation=operation)


class HitCounter(ABC):
    """
    Abstract class for a basic implementation of a HitCounter that keeps track of number of requests for different
    methods of a key-value store in past `duration_secs` seconds. The key-value store being used here is `KVStore`
    which is a toy implementation of an in-memory key-value store like Memcached or Redis.
    """

    @abstractmethod
    def __init__(self, duration_secs: int):
        pass

    @abstractmethod
    def record_hit(self, operation: KVStore.Operation) -> None:
        """
        Record a hit for the `operation`
        """
        pass

    @abstractmethod
    def get_qps(self, operation: KVStore.Operation) -> int:
        """
        Computes and returns QPS of an `operation`
        """
        pass

    @staticmethod
    def get_current_time_int() -> int:
        """
        Returns the integer value of an epoch timestamp for current time
        """
        return int(time.time())
