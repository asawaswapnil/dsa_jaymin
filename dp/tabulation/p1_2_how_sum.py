from typing import Optional, List


def how_sum_tab_look_back(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m^2 x n); O(m x n) for the loop and O(m) extra per iteration for copying the array
    Space: O(m^2)
    """
    table = [None for _ in range(target_sum + 1)]
    table[0] = []  # base case

    for ts in range(1, len(table)):
        for num in numbers:
            diff = ts - num
            if diff >= 0 and table[diff] is not None:
                table[ts] = table[diff] + [num]
                break
    return table[target_sum]


def how_sum_tab_look_ahead(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m^2 x n); O(m x n) for the loop and O(m) extra per iteration for copying the array
    Space: O(m^2); the table is O(m) and in worst case, each element in table can be an array of size `m`
    """
    table = [None for _ in range(target_sum + 1)]
    table[0] = []  # base case

    for ts in range(len(table)):
        if table[ts] is not None:
            for num in numbers:
                possible_sum = ts + num
                if possible_sum < len(table):
                    table[possible_sum] = table[ts] + [num]
    return table[target_sum]


if __name__ == '__main__':
    # P1_2 in target-sum series - combinatorics problem
    # Given an array of non-negative integers, return a subset of array that can generate a target sum otherwise return None
    # The array can contain duplicate numbers and the numbers can be reused as well
    # The array can be its own subset=-
    # If there are multiple results, return any one
    print(how_sum_tab_look_back(7, [2, 3]))  # [3, 2, 2]
    print(how_sum_tab_look_back(7, [5, 3, 4, 7]))  # [4, 3] or [7]
    print(how_sum_tab_look_back(7, [2, 4]))  # None
    print(how_sum_tab_look_back(8, [2, 3, 5]))  # [2, 2, 2, 2] or [2, 3, 3] or [3, 5]
    print(how_sum_tab_look_back(300, [1, 298]))  # [298, 1, 1] or [1] * 300
    print(how_sum_tab_look_back(300, [7, 14]))  # None
    print()
    print(how_sum_tab_look_ahead(7, [2, 3]))  # [3, 2, 2]
    print(how_sum_tab_look_ahead(7, [5, 3, 4, 7]))  # [4, 3] or [7]
    print(how_sum_tab_look_ahead(7, [2, 4]))  # None
    print(how_sum_tab_look_ahead(8, [2, 3, 5]))  # [2, 2, 2, 2] or [2, 3, 3] or [3, 5]
    print(how_sum_tab_look_ahead(300, [1, 298]))  # [298, 1, 1] or [1] * 300
    print(how_sum_tab_look_ahead(300, [7, 14]))  # None
