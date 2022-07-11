from typing import List


def split_array(nums: List[int], m: int) -> int:
    """
    Time: O(n logs) where `s` is the sum of all numbers (max possible split sum)
    Space: O(1)
    """

    def can_split(sum_threshold):
        splits = 1
        total = 0
        for num in nums:
            total += num
            if total > sum_threshold:
                total = num
                splits += 1
                if splits > m:
                    return False
        return True

    min_sum, max_sum = max(nums), sum(nums)
    while min_sum < max_sum:
        new_sum = (min_sum + max_sum) // 2
        if can_split(new_sum):
            # can definitely split for all sums greater than the new sum; check left
            max_sum = new_sum
        else:
            # can't find a possible split with new sum and all possible sums less than new sum; check right
            min_sum = new_sum + 1

    return min_sum


if __name__ == '__main__':
    print(split_array(nums=[7, 2, 5, 10, 8], m=2))  # 18
    print(split_array(nums=[1, 2, 3, 4, 5], m=2))  # 9
    print(split_array(nums=[1, 4, 4], m=3))  # 4
