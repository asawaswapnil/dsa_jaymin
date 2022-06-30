from typing import Optional, List


def best_sum_tab_look_back(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m^2 x n)
    Space: O(m^2)
    """
    table = [None for _ in range(target_sum + 1)]
    table[0] = []  # base case

    for ts in range(1, len(table)):
        for num in numbers:
            diff = ts - num
            if diff >= 0 and table[diff] is not None:
                new_combination = table[diff] + [num]
                if not table[ts] or len(new_combination) < len(table[ts]):
                    table[ts] = new_combination
    return table[target_sum]


def best_sum_tab_look_ahead(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m^2 x n)
    Space: O(m^2)
    """
    table = [None for _ in range(target_sum + 1)]
    table[0] = []  # base case

    for ts in range(len(table)):
        if table[ts] is not None:
            for num in numbers:
                possible_sum = ts + num
                if possible_sum < len(table):
                    new_combination = table[ts] + [num]
                    if not table[possible_sum] or len(new_combination) < len(table[possible_sum]):
                        table[possible_sum] = new_combination
    return table[target_sum]


if __name__ == '__main__':
    # P1_3 in target-sum series - optimization problem
    # Given an array of non-negative integers, return the smallest subset of array that can generate a target sum otherwise return None
    # The array can contain duplicate numbers and the numbers can be reused as well
    # The array can be its own subset
    # If there are multiple results with same number of elements, return any one
    print(best_sum_tab_look_back(7, [2, 3]))  # [3, 2, 2]
    print(best_sum_tab_look_back(7, [5, 3, 4, 7]))  # [7]
    print(best_sum_tab_look_back(7, [2, 4]))  # None
    print(best_sum_tab_look_back(8, [2, 3, 5]))  # [3, 5]
    print(best_sum_tab_look_back(8, [1, 4, 5]))  # [4, 4]
    print(best_sum_tab_look_back(300, [1, 298]))  # [298, 1, 1]
    print(best_sum_tab_look_back(300, [7, 14]))  # None
    print(best_sum_tab_look_back(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
    print()
    print(best_sum_tab_look_ahead(7, [2, 3]))  # [3, 2, 2]
    print(best_sum_tab_look_ahead(7, [5, 3, 4, 7]))  # [7]
    print(best_sum_tab_look_ahead(7, [2, 4]))  # None
    print(best_sum_tab_look_ahead(8, [2, 3, 5]))  # [3, 5]
    print(best_sum_tab_look_ahead(8, [1, 4, 5]))  # [4, 4]
    print(best_sum_tab_look_ahead(300, [1, 298]))  # [298, 1, 1]
    print(best_sum_tab_look_ahead(300, [7, 14]))  # None
    print(best_sum_tab_look_ahead(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]

