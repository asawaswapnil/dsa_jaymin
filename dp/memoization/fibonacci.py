from typing import Dict
from functools import lru_cache


def fib(n: int) -> int:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    Time: O(2^n)
    Space: O(n)
    """
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)


@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    """
    Memoized solution with built-in Python cache – time = num of nodes in the optimized tree, space = height of tree
    If the arguments of the recursive function are hashable, a simple lru_cache can be used to cache function calls
    Setting maxsize as None disables all LRU features making it a simple memo/cache
    Time: O(n)
    Space: O(n)
    """
    if n <= 2:
        return 1
    return fib_cached(n-2) + fib_cached(n-1)


def fib_memo(n: int, memo: Dict[int, int]) -> int:
    """
    Memoized solution with a dictionary – time = num of nodes in the optimized tree, space = height of tree
    Time: O(n)
    Space: O(n)
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-2, memo) + fib_memo(n-1, memo)
    return memo[n]


if __name__ == '__main__':
    # Num: 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, ..., 50,          ...
    # Seq: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..., 12586269025, ...
    print(fib_memo(6, {}))
    print(fib_memo(7, {}))
    print(fib_memo(8, {}))
    print(fib_memo(50, {}))
