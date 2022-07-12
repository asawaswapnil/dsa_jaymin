from typing import List


def min_days(bloom_days: List[int], m: int, k: int) -> int:
    """
    Time: O(n logm)
    Space: O(1)
    """

    def possible_to_make_m_bouquets(days):
        bouquets = 0
        adjacent_flowers = 0
        for day in bloom_days:
            if day > days:
                adjacent_flowers = 0
                continue
            adjacent_flowers += 1
            if adjacent_flowers == k:
                bouquets += 1
                if bouquets == m:
                    return True
                adjacent_flowers = 0
        return False

    if len(bloom_days) < m * k:
        return -1

    left, right = min(bloom_days), max(bloom_days)

    while left < right:
        n_days = (left + right) // 2
        if possible_to_make_m_bouquets(n_days):
            right = n_days
        else:
            left = n_days + 1

    return left


if __name__ == '__main__':
    print(min_days(bloom_days=[1, 10, 3, 10, 2], m=3, k=1))  # 3
    print(min_days(bloom_days=[1, 10, 3, 10, 2], m=3, k=2))  # -1
    print(min_days(bloom_days=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))  # 12
