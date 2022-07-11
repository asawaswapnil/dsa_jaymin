def binary_search(nums, n):
    """
    Time: O(log n)
    Space: O(1)
    """
    def number_exists_in_left_subarray(idx) -> bool:
        return n <= nums[idx]

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if number_exists_in_left_subarray(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    """
    Toy application of the binary search template
    Given a sorted array `nums` and some number `n` in the array, find the index of `n`
    """
    nums, n = [1, 2, 3, 4, 5, 6], 4
    print(binary_search(nums, n))
