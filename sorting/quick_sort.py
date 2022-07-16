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
        pivot_idx = _partition(array, first, last)
        _quick_sort(array, first, pivot_idx - 1)
        _quick_sort(array, pivot_idx + 1, last)
    return array


def _partition(array: List, first: int, last: int):
    """
    - Take last (rightmost) element as pivot
    - Start with the first index as a potential pivot idx and try to find the correct index by iterating over the array
    - While iterating move all elements smaller than or equal to pivot to the left of the pivot and move pivot idx to
        the right one place at a time
    - After one pass over the array (array[left .. right]), the pivot idx will be at the correct position for the pivot
        element; perform one final swap to put the pivot element in its correct place
    """
    pivot = array[last]
    pivot_idx = first
    for idx in range(first, last):
        if array[idx] <= pivot:
            array[idx], array[pivot_idx] = array[pivot_idx], array[idx]
            pivot_idx += 1
    # here `pivot_idx` is the correct index for the pivot element and `last` is where the pivot element currently resides
    # swap them to get pivot element in its corrrect place in the array and return the pivot idx
    array[pivot_idx], array[last] = array[last], array[pivot_idx]
    return pivot_idx


if __name__ == '__main__':
    unsorted_array = [1, 4, 7, 4, 5, 8, 3, 10, 5, 100, -1]
    print(quick_sort(unsorted_array))
