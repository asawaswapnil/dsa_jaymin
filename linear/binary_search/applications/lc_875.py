import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Time: O(n logm) where m is the search-space of min possible -> max possible speed
    Space: O(1)
    """

    def can_finish(speed):
        time_taken = 0
        for pile in piles:
            time_taken += math.ceil(pile / speed)
            if time_taken > h:
                return False
        return True

    min_speed, max_speed = 1, max(piles)

    while min_speed < max_speed:
        new_speed = (min_speed + max_speed) // 2
        if can_finish(new_speed):
            max_speed = new_speed
        else:
            min_speed = new_speed + 1

    return min_speed


if __name__ == '__main__':
    print(min_eating_speed(piles=[3, 6, 7, 11], h=8))  # 4
    print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=5))  # 30
    print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=6))  # 23
