from typing import List
from itertools import accumulate


def counting_sort(array: List) -> List:
    """
    Counting Sort
    Time: O(n + k)
    Space: O(k)
    """
    k = max(array)
    counts = [0 for _ in range(k + 1)]
    for num in array:
        counts[num] += 1

    running_counts = list(accumulate(counts))
    results = [None for _ in range(len(array))]
    for idx in range(len(array) - 1, -1, -1):  # iterate in reversed fashion to maintain stable sorting order
        num = array[idx]
        position = running_counts[num] - 1
        results[position] = num
        running_counts[num] -= 1

    return results


if __name__ == '__main__':
    unsorted_array = [1, 4, 7, 4, 5, 8, 3, 10, 5, 100]
    print(counting_sort(unsorted_array))
