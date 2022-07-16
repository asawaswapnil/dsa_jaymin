from typing import List
from collections import deque


def radix_sort(array: List, base: int) -> List:
    """
    Radix Sort (for decimal numbers)
    Time: O(maxd * n) => O(n); `maxd` is the number of digits in the largest number in array
    Space: O(base + n) => O(10 + n) => O(n); where base is nthe base of the number system being used,
        2 for binary, 8 for octal, 16 for haxadecimal, 10 for decimal, etc.
    """
    max_digits = len(str(max(array)))
    bins = [deque([]) for _ in range(base)]

    for d in range(max_digits):
        # binning
        for num in array:
            _bin = (num // (base ** d)) % base
            bins[_bin].append(num)
        # collecting
        array.clear()
        for _bin in bins:
            while _bin:
                array.append(_bin.popleft())

    return array


if __name__ == '__main__':
    unsorted_array = [11, 41, 17, 49, 56, 80, 3, 1, 562, 100]
    print(radix_sort(unsorted_array, base=10))
