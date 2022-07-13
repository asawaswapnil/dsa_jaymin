from __future__ import annotations

from threading import RLock
from typing import Dict, List

from misc.hit_counter import HitCounter, KVStore


class HitCounterRing(HitCounter):
    """
    A thread-safe implementation of HitCounter using Ring Buffer or a Circular Queue.

    It maintains two fixed size buffers, one to keep track of timestamp and other to keep track of number of hits

    Runtime complexities:
    All operations on buffer are indexed and take amortized O(1) time. While calculating QPS, we iterate over fixed size
    buffers which is also O(1).
    The space complexity is also O(1) since at most there will be `duration_secs` elements in the buffers.
    """

    def __init__(self, duration_secs: int):
        self._duration: int = duration_secs
        self._hits: Dict[KVStore.Operation, List[int]] = {
            op: [0 for _ in range(self._duration)] for op in KVStore.Operation
        }
        self._times: Dict[KVStore.Operation, List[int]] = {
            op: [None for _ in range(self._duration)] for op in KVStore.Operation
        }
        self._locks: Dict[KVStore.Operation, RLock] = {
            op: RLock() for op in KVStore.Operation
        }

    def record_hit(self, operation: KVStore.Operation) -> None:
        """
        Record a hit for the `operation`
        """
        current_time = self.get_current_time_int()
        hits = self._hits[operation]
        times = self._times[operation]
        idx = current_time % self._duration

        with self._locks[operation]:
            if times[idx] != current_time:
                times[idx] = current_time
                hits[idx] = 1
            else:
                hits[idx] += 1

    def get_qps(self, operation: KVStore.Operation) -> int:
        """
        Computes and returns QPS of an `operation`
        """
        current_time = self.get_current_time_int()
        hits = self._hits[operation]
        times = self._times[operation]

        with self._locks[operation]:
            total_hits = 0
            earliest_ts = current_time
            for idx in range(self._duration):
                if times[idx] and current_time - times[idx] <= self._duration:
                    earliest_ts = min(earliest_ts, times[idx])
                    total_hits += hits[idx]
            total_secs = (current_time - earliest_ts) or 1
            return total_hits // total_secs
