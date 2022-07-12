import math
from typing import List


def smallest_divisor(nums: List[int], threshold: int) -> int:
    def can_divide(divisor):
        result = sum(map(lambda n: math.ceil(n / divisor), nums))
        return result <= threshold

    left, right = 1, max(nums)

    while left < right:
        divisor = (left + right) // 2
        if can_divide(divisor):
            right = divisor
        else:
            left = divisor + 1

    return left


if __name__ == '__main__':
    print(smallest_divisor(nums=[1, 2, 5, 9], threshold=6))  # 5
    print(smallest_divisor(nums=[44, 22, 33, 11, 1], threshold=5))  # 44
