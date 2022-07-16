from typing import List


def quick_sort(array: List) -> List:
    """
    Quick Sort
    Time: best case O(n logn), worst case O(n^2)
    Space: O(logn)
    """
    first, last = 0, len(array) - 1
    return _quick_sort(array, first, last)


def _quick_sort(array: List, first: int, last: int) -> List:
    if first < last:
        split = _partition(array, first, last)
        _quick_sort(array, first, split - 1)
        _quick_sort(array, split + 1, last)
    return array


def _partition(array: List, first: int, last: int):
    pivot, pivot_idx = array[first], first
    while first <= last:
        while first <= last and array[first] <= pivot:
            first += 1
        while first <= last and array[last] >= pivot:
            last -= 1
        if first <= last:
            array[first], array[last] = array[last], array[first]
    array[pivot_idx], array[last] = array[last], array[pivot_idx]
    return last


if __name__ == '__main__':
    unsorted_array = [1, 4, 7, 4, 5, 8, 3, 10, 5, 100, -1]
    print(quick_sort(unsorted_array))
