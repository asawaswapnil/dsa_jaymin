from typing import List, Tuple, Union


def find_word_locations(grid: List[List[str]], word: str) -> List[Tuple]:
    """
    Time: O(m x n x l), where `l` is length of word
    Space: O(m x n x l), where `l` is length of word
    """
    def _search(row: int, col: int, idx: int, path: List[Tuple]) -> Union[None, List[Tuple]]:
        key = (row, col, idx)
        if key in memo:
            return memo[key]
        elif idx == len(word):
            return path
        elif not 0 <= row < ROWS or not 0 <= col < COLS:
            memo[key] = None
        elif grid[row][col] != word[idx] or grid[row][col] == PATH_MARKER:
            memo[key] = None
        else:
            grid[row][col] = PATH_MARKER
            memo[key] = \
                _search(row, col + 1, idx + 1, path + [(row, col)]) or \
                _search(row, col - 1, idx + 1, path + [(row, col)]) or \
                _search(row + 1, col, idx + 1, path + [(row, col)]) or \
                _search(row - 1, col, idx + 1, path + [(row, col)])
            grid[row][col] = word[idx]
        return memo[key]

    if not word or not grid or not grid[0]:
        return []

    PATH_MARKER = "#"
    ROWS, COLS = len(grid), len(grid[0])
    memo = {}
    for row in range(ROWS):
        for col in range(COLS):
            _search(row, col, 0, [])
            if memo[(row, col, 0)] is not None:
                return memo[(row, col, 0)]
    return []


def test_find_word_locations_word_exists_right_down():
    grid = [
        ["a", "b", "k", "c", "j", "p", "l"],
        ["d", "v", "d", "a", "t", "n", "i"],
        ["x", "a", "d", "t", "n", "i", "q"],
        ["f", "d", "d", "n", "b", "n", "g"],
        ["a", "b", "k", "i", "p", "p", "l"],
        ["d", "v", "d", "h", "c", "f", "n"],
        ["x", "a", "d", "w", "s", "b", "q"]
    ]
    word = "catnip"
    locations = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_word_exists_all_directions():
    grid = [
        ["a", "b", "a", "l", "n", "o", "l"],
        ["d", "v", "d", "l", "i", "s", "i"],
        ["x", "a", "d", "t", "n", "i", "q"],
        ["f", "d", "d", "n", "b", "n", "g"],
        ["a", "b", "k", "i", "a", "p", "l"],
        ["d", "v", "d", "h", "c", "f", "n"],
        ["x", "a", "d", "w", "s", "b", "q"]
    ]
    word = "allison"
    locations = [(0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (0, 5), (0, 4)]
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_word_exists_all_directions_overlap():
    grid = [
        ["a", "b", "t", "e", "n", "o", "l"],
        ["d", "v", "i", "b", "i", "s", "i"],
        ["x", "a", "d", "t", "n", "i", "q"],
        ["f", "d", "d", "n", "b", "n", "g"],
        ["a", "b", "k", "i", "a", "p", "l"],
        ["d", "v", "d", "h", "c", "f", "n"],
        ["x", "a", "d", "w", "s", "b", "q"]
    ]
    word = "tibet"
    locations = []
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_word_does_not_exist():
    grid = [
        ["a", "b", "k", "c", "j", "p", "l"],
        ["d", "v", "d", "a", "t", "n", "i"],
        ["x", "a", "d", "t", "n", "i", "q"],
        ["f", "d", "d", "n", "b", "n", "g"],
        ["a", "b", "o", "i", "p", "p", "l"],
        ["d", "v", "d", "h", "c", "f", "n"],
        ["x", "a", "d", "w", "s", "b", "q"]
    ]
    word = "dog"
    locations = []
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_empty_grid():
    grid = []
    word = "dog"
    locations = []
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_empty_cols():
    grid = [[], [], []]
    word = "dog"
    locations = []
    assert find_word_locations(grid, word) == locations


def test_find_word_locations_empty_word():
    grid = [
        ["a", "b", "c"],
        ["a", "b", "c"],
        ["a", "b", "c"]
    ]
    word = ""
    locations = []
    assert find_word_locations(grid, word) == locations


if __name__ == '__main__':
    test_find_word_locations_word_exists_right_down()
    test_find_word_locations_word_exists_all_directions()
    test_find_word_locations_word_exists_all_directions_overlap()
    test_find_word_locations_word_does_not_exist()
    test_find_word_locations_empty_grid()
    test_find_word_locations_empty_cols()
    test_find_word_locations_empty_word()
