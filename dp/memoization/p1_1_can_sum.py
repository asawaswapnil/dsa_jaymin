from typing import List, Dict


def can_sum(target_sum: int, numbers: List[int]) -> bool:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    If `n` is length of numbers array and `m` is the target sum
    Time: O(n^m); we subtract each num in array from target sum and branch
    Space: O(m); in worst case an array can be [1]
    """
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        diff = target_sum - num
        if can_sum(diff, numbers):
            return True
    return False


def can_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, bool]) -> bool:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m x n); even though we don't look at already computed target sums but at each level it might still be
        required to create multiple branches de[ending on the target sum for that node and the numbers in array
    Space: O(m); in worst case an array can be [1]
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        diff = target_sum - num
        if can_sum_memo(diff, numbers, memo):
            memo[target_sum] = True
            return memo[target_sum]
    memo[target_sum] = False
    return memo[target_sum]


if __name__ == '__main__':
    # P1_1 in target-sum series - decision problem
    # Given an array of non-negative integers, return if it's possible to generate a target sum using numbers in the array.
    # The array can contain duplicate numbers and the numbers can be reused as well
    print(can_sum_memo(7, [2, 3], {}))  # True
    print(can_sum_memo(7, [5, 3, 4, 7], {}))  # True
    print(can_sum_memo(7, [2, 4], {}))  # False
    print(can_sum_memo(8, [2, 3, 5], {}))  # True
    print(can_sum_memo(300, [1, 298], {}))  # True
    print(can_sum_memo(300, [7, 14], {}))  # False
