from typing import List


def merge_sort(array: List) -> List:
    """
    Merge Sort
    Time: O(nlogn)
    Space: O(n + logn)
    """
    if len(array) > 1:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        array = _merge(left, right)
    return array


def _merge(left_array: List, right_array: List) -> List:
    """
    Merge two sorted lists
    """
    i = j = 0
    result = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    result += left_array[i:] + right_array[j:]
    return result


if __name__ == '__main__':
    unsorted_array = [1, 4, 7, 4, 5, 8, 3, 10, 5, 100, -1]
    print(merge_sort(unsorted_array))
