from __future__ import annotations

import time

from misc.hit_counter import KVStore
from misc.hit_counter.hit_counter_deque import HitCounterDeque
from misc.hit_counter.hit_counter_ring import HitCounterRing


if __name__ == '__main__':
    DURATION_SECS = 2

    for hc_impl in [HitCounterRing, HitCounterDeque]:
        print("\nType: {}".format(hc_impl.__name__))
        start = time.perf_counter()

        kv_store = KVStore(hit_counter_impl=hc_impl, hit_tracking_duration=DURATION_SECS)
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

        _total_sleep_time = DURATION_SECS + 1
        print("Time taken: {}\n".format(time.perf_counter() - start - _total_sleep_time))
