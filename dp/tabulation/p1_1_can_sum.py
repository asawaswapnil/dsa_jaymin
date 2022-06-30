from typing import List


def can_sum_tab_look_back(target_sum: int, numbers: List[int]) -> bool:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m x n)
    Space: O(m)
    """
    table = [False for _ in range(target_sum + 1)]
    table[0] = True  # base case

    for ts in range(1, len(table)):
        for num in numbers:
            diff = ts - num
            if diff >= 0 and table[diff]:
                table[ts] = True
                break

    return table[target_sum]


def can_sum_tab_look_ahead(target_sum: int, numbers: List[int]) -> bool:
    """
    Tabulated solution
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m x n)
    Space: O(m)
    """
    table = [False for _ in range(target_sum + 1)]
    table[0] = True  # base case

    for ts in range(len(table)):
        if table[ts]:
            for num in numbers:
                possible_sum = ts + num
                if possible_sum < len(table):
                    table[possible_sum] = True
    return table[target_sum]


if __name__ == '__main__':
    # P1_1 in target-sum series - decision problem
    # Given an array of non-negative integers, return if it's possible to generate a target sum using numbers in the array.
    # The array can contain duplicate numbers and the numbers can be reused as well
    print(can_sum_tab_look_back(7, [2, 3]))  # True
    print(can_sum_tab_look_back(7, [5, 3, 4, 7]))  # True
    print(can_sum_tab_look_back(7, [2, 4]))  # False
    print(can_sum_tab_look_back(8, [2, 3, 5]))  # True
    print(can_sum_tab_look_back(300, [1, 298]))  # True
    print(can_sum_tab_look_back(300, [7, 14]))  # False
    print()
    print(can_sum_tab_look_ahead(7, [2, 3]))  # True
    print(can_sum_tab_look_ahead(7, [5, 3, 4, 7]))  # True
    print(can_sum_tab_look_ahead(7, [2, 4]))  # False
    print(can_sum_tab_look_ahead(8, [2, 3, 5]))  # True
    print(can_sum_tab_look_ahead(300, [1, 298]))  # True
    print(can_sum_tab_look_ahead(300, [7, 14]))  # False
