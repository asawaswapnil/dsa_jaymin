def sqrt_int(x: int) -> int:
    """
    Time: O(log x)
    Space: O(1)
    """
    left, right = 0, x + 1  # right = x + 1 instead of x to handle the case when x = 1

    while left < right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1

    return left - 1  # `left` is the minimum k value, `k - 1` is the answer


if __name__ == '__main__':
    print(sqrt_int(4))  # 2
    print(sqrt_int(8))  # 2
    print(sqrt_int(9))  # 3
    print(sqrt_int(100))  # 10
    print(sqrt_int(150))  # 12
