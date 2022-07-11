import math
from typing import List


def ship_within_days(weights: List[int], days: int) -> int:
    """
    Time: O(n logm) where m is the search-space
    Space: O(1)
    """

    def can_ship_in_time(capacity):
        num_days = 1
        daily_weight = 0
        for package_weight in weights:
            daily_weight += package_weight
            if daily_weight > capacity:
                daily_weight = package_weight
                num_days += 1
                if num_days > days:
                    return False
        return True

    min_capacity = max(weights)
    max_capacity = math.ceil(len(weights) / days) * max(weights)

    while min_capacity < max_capacity:
        new_capacity = (min_capacity + max_capacity) // 2
        if can_ship_in_time(new_capacity):
            max_capacity = new_capacity
        else:
            min_capacity = new_capacity + 1

    return min_capacity


if __name__ == '__main__':
    print(ship_within_days(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))  # 15
    print(ship_within_days(weights=[3, 2, 2, 4, 1, 4], days=3))  # 6
    print(ship_within_days(weights=[1, 2, 3, 1, 1], days=4))  # 3
