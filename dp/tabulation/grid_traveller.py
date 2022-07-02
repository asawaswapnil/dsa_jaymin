
def grid_traveller_tab_look_back(m: int, n: int) -> int:
    """
    Tabulated solution
    Time: O(m x n)
    Space: O(m x n)
    """
    ROWS, COLS = m + 1, n + 1
    table = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    table[0][0], table[1][1] = 0, 1  # base cases
    for row in range(1, ROWS):
        for col in range(1, COLS):
            table[row][col] += table[row][col - 1]  # left
            table[row][col] += table[row - 1][col]  # up
    return table[m][n]


def grid_traveller_tab_look_ahead(m: int, n: int) -> int:
    """
    Tabulated solution
    Time: O(m x n)
    Space: O(m x n)
    """
    ROWS, COLS = m + 1, n + 1
    table = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    table[0][0], table[1][1] = 0, 1  # base cases
    for row in range(ROWS):
        for col in range(COLS):
            if col + 1 < COLS:  # right
                table[row][col + 1] += table[row][col]
            if row + 1 < ROWS:  # down
                table[row + 1][col] += table[row][col]
    return table[m][n]


def grid_traveller_tab_optimized(m: int, n: int) -> int:
    """
    Tabulated solution
    Time: O(m x n)
    Space: O(min(m, n))
    """
    if m < n:  # number of rows should always be >= number of cols
        m, n = n, m
    ROWS, COLS = m + 1, n + 1
    prev_row = [0 for _ in range(COLS)]
    curr_row = [0 for _ in range(COLS)]
    for row in range(1, ROWS):
        for col in range(1, COLS):
            if row == 1 and col == 1:
                curr_row[col] = 1
            else:
                curr_row[col] = curr_row[col - 1] + prev_row[col]  # left + up
        # we are anyway always assigning (=) the values in current row
        # so using previous row as current row works because all the exiting values will be replaced by the new values
        prev_row, curr_row = curr_row, prev_row
    return prev_row[n]


if __name__ == '__main__':
    # Given an (m x n) grid, find number of ways to reach from top left to bottom right
    # You are only allowed to move down or right
    print(grid_traveller_tab_look_back(1, 2))  # 1
    print(grid_traveller_tab_look_back(2, 3))  # 3
    print(grid_traveller_tab_look_back(3, 2))  # 3
    print(grid_traveller_tab_look_back(3, 3))  # 6
    print(grid_traveller_tab_look_back(4, 4))  # 20
    print(grid_traveller_tab_look_back(18, 18))  # 2333606220
    print()
    print(grid_traveller_tab_look_ahead(1, 2))  # 1
    print(grid_traveller_tab_look_ahead(2, 3))  # 3
    print(grid_traveller_tab_look_ahead(3, 2))  # 3
    print(grid_traveller_tab_look_ahead(3, 3))  # 6
    print(grid_traveller_tab_look_ahead(4, 4))  # 20
    print(grid_traveller_tab_look_ahead(18, 18))  # 2333606220
    print()
    print(grid_traveller_tab_optimized(1, 2))  # 1
    print(grid_traveller_tab_optimized(2, 3))  # 3
    print(grid_traveller_tab_optimized(3, 2))  # 3
    print(grid_traveller_tab_optimized(3, 3))  # 6
    print(grid_traveller_tab_optimized(4, 4))  # 20
    print(grid_traveller_tab_optimized(18, 18))  # 2333606220
