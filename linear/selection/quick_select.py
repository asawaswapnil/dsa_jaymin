from typing import List
from enum import Enum


class Selection(Enum):
    SMALLEST = 0
    LARGEST = 1


def quick_select(array: List, selection: Selection, k: int) -> int:
    """
    Quick Select from an unsorted array
    Time: best and average case O(n), worst case O(n^2)
    Space: O(1)
    """
    first, last = 0, len(array) - 1
    if selection == Selection.SMALLEST:
        k -= 1  # array indices start from 0
        return _select_kth_smallest_iterative(array, first, last, k)
    else:
        k = len(array) - k  # kth largest is (n-k)th smallest
        return _select_kth_smallest_iterative(array, first, last, k)


def _select_kth_smallest_recursive(array: List, first: int, last: int, k: int) -> int:
    """
    Find kth smallest element from the array
    """
    pivot_idx = _partition(array, first, last)
    if k < pivot_idx:
        return _select_kth_smallest_recursive(array, first, pivot_idx - 1, k)
    elif k > pivot_idx:
        return _select_kth_smallest_recursive(array, pivot_idx + 1, last, k)
    else:
        return array[pivot_idx]


def _select_kth_smallest_iterative(array: List, first: int, last: int, k: int) -> int:
    """
    Find kth smallest element from the array
    """
    while first <= last:
        pivot_idx = _partition(array, first, last)
        if k < pivot_idx:
            last = pivot_idx - 1
        elif k > pivot_idx:
            first = pivot_idx + 1
        else:
            return array[pivot_idx]


def _partition(array: List, first: int, last: int) -> int:
    """
    Partition the array and return the pivot index such that everything to the left of the partition (pivot) index is
        less than or equal to the element at the pivot index and everything to the right is greated than the pivor index
    Algorithm:
    - Take last (rightmost) element as pivot
    - Start with the first index as a potential pivot idx and try to find the correct index by iterating over the array
    - While iterating move all elements smaller than or equal to pivot to the left of the pivot and move pivot idx to
        the right one place at a time
    - After one pass over the array (array[first .. last]), the pivot idx will be at the correct position for the pivot
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
    print("\nUnsorted Array: {}".format(unsorted_array))
    print("Sorted Array: {} (for reference)".format(sorted(unsorted_array)))
    print("\nSelect 1st largest from unsorted array: {}".format(quick_select(unsorted_array, selection=Selection.LARGEST, k=1)))
    print("Select 1st smallest from unsorted array: {}".format(quick_select(unsorted_array, selection=Selection.SMALLEST, k=1)))
    print("Select 5th largest from unsorted array: {}".format(quick_select(unsorted_array, selection=Selection.LARGEST, k=5)))
    print("Select 3rd smallest from unsorted array: {}".format(quick_select(unsorted_array, selection=Selection.SMALLEST, k=3)))
