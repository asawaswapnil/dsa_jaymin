from typing import Optional, List, Dict


def how_sum(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    If `n` is length of numbers array and `m` is the target sum
    Time: O(n^m x m); we subtract each num in array from target sum and branch so O(n^m) and we also need O(m) for
        copying elements while creating new arrays (result + [num])
    Space: O(m); in worst case an array can be [1] (so O(m)) and O(m) extra space just once for the result array
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        diff = target_sum - num
        result = how_sum(diff, numbers)
        if result is not None:
            return result + [num]
    return None


def how_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    If `n` is length of numbers array and `m` is the target sum
    Time: O(m^2 x n); even though we don't look at already computed target sums but at each level it might still be
        required to create multiple branches depending on the target sum for that node and the numbers in array (so O(m x n)),
        and we also need O(m) for copying elements while creating new arrays (result + [num])
    Space: O(m^2); in worst case an array can be [1] (so O(m)), we also need O(m x m) (or O(m^2)) extra space for the memo
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        diff = target_sum - num
        result = how_sum_memo(diff, numbers, memo)
        if result is not None:
            memo[target_sum] = result + [num]
            return memo[target_sum]
    memo[target_sum] = None
    return memo[target_sum]


if __name__ == '__main__':
    # P1_2 in target-sum series - combinatorics problem
    # Given an array of non-negative integers, return a subset of array that can generate a target sum otherwise return None
    # The array can contain duplicate numbers and the numbers can be reused as well
    # The array can be its own subset
    # If there are multiple results, return any one
    print(how_sum_memo(7, [2, 3], {}))  # [3, 2, 2]
    print(how_sum_memo(7, [5, 3, 4, 7], {}))  # [4, 3] or [7]
    print(how_sum_memo(7, [2, 4], {}))  # None
    print(how_sum_memo(8, [2, 3, 5], {}))  # [2, 2, 2, 2] or [2, 3, 3] or [3, 5]
    print(how_sum_memo(300, [1, 298], {}))  # [298, 1, 1] or [1] * 300
    print(how_sum_memo(300, [7, 14], {}))  # None
