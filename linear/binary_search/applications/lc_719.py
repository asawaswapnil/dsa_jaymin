from typing import List


def smallest_distance_pair(nums: List[int], k: int) -> int:
    def has_k_or_more_pairs_with_smaller_distance_than(d):
        pairs = 0
        i, j = 0, 1
        while i < n:
            while j < n and nums[j] - nums[i] <= d:
                j += 1
            pairs += (j - 1) - i  # j - 1 because nums[j] - nums[i] was true for the previous value of j
            if pairs >= k:
                return True
            i += 1
        return False

    nums.sort()
    n = len(nums)
    left, right = 0, nums[-1] - nums[0]

    while left < right:
        distance = (left + right) // 2
        if has_k_or_more_pairs_with_smaller_distance_than(distance):
            right = distance
        else:
            left = distance + 1

    return left


if __name__ == '__main__':
    print(smallest_distance_pair(nums=[1, 1, 1], k=2))  # 0
    print(smallest_distance_pair(nums=[1, 6, 1], k=3))  # 5
