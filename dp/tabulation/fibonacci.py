
def fib_tab_look_back(n: int) -> int:
    """
    Tabulated solution
    Time: O(n)
    Space: O(n)
    """
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1  # base cases
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_tab_look_ahead(n: int) -> int:
    """
    Tabulated solution
    Time: O(n)
    Space: O(n)
    """
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1  # base cases
    for i in range(n):
        if i + 1 < len(table):
            table[i + 1] += table[i]
        if i + 2 < len(table):
            table[i + 2] += table[i]
    return table[n]


def fib_tab_look_back_optimized(n: int) -> int:
    """
    Optimized tabulated solution
    Time: O(n)
    Space: O(1)
    """
    table = [0, 1]
    for i in range(2, n + 1):
        table[0], table[1] = table[1], sum(table)
    return table[1]


if __name__ == '__main__':
    # Num: 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, ..., 50,          ...
    # Seq: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..., 12586269025, ...
    print(fib_tab_look_back(6))  # 8
    print(fib_tab_look_back(7))  # 13
    print(fib_tab_look_back(8))  # 21
    print(fib_tab_look_back(50))  # 12586269025
    print()
    print(fib_tab_look_ahead(6))  # 8
    print(fib_tab_look_ahead(7))  # 13
    print(fib_tab_look_ahead(8))  # 21
    print(fib_tab_look_ahead(50))  # 12586269025
    print()
    print(fib_tab_look_back_optimized(6))  # 8
    print(fib_tab_look_back_optimized(7))  # 13
    print(fib_tab_look_back_optimized(8))  # 21
    print(fib_tab_look_back_optimized(50))  # 12586269025
