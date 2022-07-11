from typing import List


def search_insert_position(nums: List[int], target: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums)  # target can be to the right of aray so `right` is len(nums) instead of len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(search_insert_position(nums=[1, 3, 5, 6], target=5))  # 2
    print(search_insert_position(nums=[1, 3, 5, 6], target=2))  # 1
    print(search_insert_position(nums=[1, 3, 5, 6], target=1))  # 0
    print(search_insert_position(nums=[1, 3, 5, 6], target=7))  # 4
