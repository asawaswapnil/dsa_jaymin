import math


def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:
    def has_n_ugly_numbers_less_than(num) -> bool:
        total = num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc
        return total >= n

    ab = a * b // math.gcd(a, b)
    ac = a * c // math.gcd(a, c)
    bc = b * c // math.gcd(b, c)
    abc = a * bc // math.gcd(a, bc)

    left, right = min(a, b, c), 2 * (10 ** 9)
    while left < right:
        num = left + (right - left) // 2
        if has_n_ugly_numbers_less_than(num):
            right = num
        else:
            left = num + 1
    return left


if __name__ == '__main__':
    print(nth_ugly_number(n=3, a=2, b=3, c=5))  # 4
    print(nth_ugly_number(n=4, a=2, b=3, c=4))  # 6
    print(nth_ugly_number(n=5, a=2, b=11, c=13))  # 10

