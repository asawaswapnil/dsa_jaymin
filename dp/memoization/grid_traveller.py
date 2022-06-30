from typing import Dict, Tuple


def grid_traveller(m: int, n: int) -> int:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    Time: O(2^(m+n))
    Space: O(m + n)
    """
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return grid_traveller(m-1, n) + grid_traveller(m, n-1)


def grid_traveller_memo(m: int, n: int, memo: Dict[Tuple, int]) -> int:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    Time: O(m x n)
    Space: O(m + n)
    """
    # number of ways to traverse (m x n) grid is same as that for an (n x m) grid, sorting prunes the problem tree even more
    key = tuple(sorted([m, n]))
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = grid_traveller_memo(m-1, n, memo) + grid_traveller_memo(m, n-1, memo)
    return memo[key]


if __name__ == '__main__':
    # Given an (m x n) grid, find number of ways to reach from top left to bottom right
    # You are only allowed to move down or right
    print(grid_traveller_memo(1, 2, {}))  # 1
    print(grid_traveller_memo(2, 3, {}))  # 3
    print(grid_traveller_memo(3, 2, {}))  # 3
    print(grid_traveller_memo(3, 3, {}))  # 6
    print(grid_traveller_memo(4, 4, {}))  # 20
    print(grid_traveller_memo(18, 18, {}))  # 2333606220
