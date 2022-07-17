
def find_nth_number(n: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    # find bucket
    power, p = 1, 0
    while p + (2 ** power) < n:
        p += (2 ** power)
        power += 1

    # find kth number from curent bucket such that `n = p + k`
    # here `p` is count of numbers present in the previous buckets
    # for example, if `n = 11`, we have already considered 2 + 4, 6 numbers in the last two buckets,
    # so we now need to find 5th number in the current bucket
    # here p = 6 and k = 5 for n = 11
    k = n - p  # remaining nums to find in the current bucket
    digits = []
    left, right = 1, 2 ** power
    while left < right:
        mid = (left + right) // 2
        if mid >= k:
            digits.append("5")
            right = mid
        else:
            digits.append("8")
            left = mid + 1

    return int("".join(digits))


if __name__ == '__main__':
    # Given an integer N, find the nth number in the increasing sequence of numbers that only contain 5 and/or 8
    # Example: for N = 11, return 855
    # 5, 8, 55, 58, 85, 88, 555, 558, 585, 588, 855, 858, 885, 888, ....
    print(find_nth_number(n=1))  # 5
    print(find_nth_number(n=2))  # 8
    print(find_nth_number(n=5))  # 85
    print(find_nth_number(n=11))  # 855
