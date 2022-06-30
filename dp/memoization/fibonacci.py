from typing import Dict


def fib(n: int) -> int:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    Time: O(2^n)
    Space: O(n)
    """
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)


def fib_memo(n: int, memo: Dict[int, int]) -> int:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
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
