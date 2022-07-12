def find_kth_number(m: int, n: int, k: int) -> int:
    """
    Time: O(mlog(mn))
    Space: O(1)
    """
    def has_k_or_more_values_before(num):
        count = 0
        for i in range(1, m + 1):
            count += min(num // i, n)  # num of values in this row
            if count >= k:  # are there k or more values until this num in total
                return True
        return False

    left, right = 1, m * n
    while left < right:
        num = (left + right) // 2
        if has_k_or_more_values_before(num):
            # there are k or more, smaller numbers until this number, search left
            right = num
        else:
            # there are less than k numbers smaller than this number, search right
            left = num + 1

    return left


if __name__ == '__main__':
    print(find_kth_number(m=3, n=3, k=5))  # 3
    print(find_kth_number(m=2, n=3, k=6))  # 6
