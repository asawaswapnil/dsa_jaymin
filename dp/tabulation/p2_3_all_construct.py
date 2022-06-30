from typing import List


def all_construct_tab_look_back(target: str, word_list: List[str]) -> List[List[str]]:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    Time: O(n^m)
    Space: ~O(m x n^m); the table is an array of `m` elements where each element is a 2D array of all (n^m) possible
        combinations; so basically a 3D table

    One this to note here is that the memoized solution runs faster but for worst case, it runs at the same time and
    space complexity as the brute force version because we have to find all possible paths in the recursion tree.
    Worst case here would be, target = "aaaaaaaaaaaaaaaaa", word_list = ["a", "aa", "aaaa", "aaaaa", "aaaaaa"]
    """
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for end_idx in range(1, len(table)):
        target_sub_str = target[:end_idx]
        for word in word_list:
            if len(word) <= len(target_sub_str):
                if len(table[end_idx - len(word)]) > 0 and target_sub_str.endswith(word):
                    table[end_idx].extend(map(lambda l: l + [word], table[end_idx - len(word)]))
    return table[len(target)]


def all_construct_tab_look_ahead(target: str, word_list: List[str]) -> List[List[str]]:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    Time: O(n^m)
    Space: ~O(m x n^m); the table is an array of `m` elements where each element is a 2D array of all (n^m) possible
        combinations; so basically a 3D table

    One this to note here is that the memoized solution runs faster but for worst case, it runs at the same time and
    space complexity as the brute force version because we have to find all possible paths in the recursion tree.
    Worst case here would be, target = "aaaaaaaaaaaaaaaaa", word_list = ["a", "aa", "aaaa", "aaaaa", "aaaaaa"]
    """
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for end_idx in range(len(table)):
        if len(table[end_idx]) > 0:
            target_sub_str = target[end_idx:]
            for word in word_list:
                if len(word) <= len(target_sub_str):
                    if target_sub_str.startswith(word):
                        table[end_idx + len(word)].extend(map(lambda l: l + [word], table[end_idx]))
    return table[len(target)]


if __name__ == '__main__':
    # P2_1 in word-construct series
    # Given a target word and a list of words, return all the ways in which the target word can be constructed from the word list
    # The result should be a 2D array where each element inside the result should represent a combination that can construct target
    # Words in the word list can be reused
    print(all_construct_tab_look_back("purple", ["purp", "p", "ur", "le", "purpl"]))
    # [
    #   ["purp", "le"],
    #   ["p", "ur", "p", "le"]
    # ]
    print(all_construct_tab_look_back("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    # [
    #   ["ab", "cd", "ef"],
    #   ["ab", "c", "def"],
    #   ["abc", "def"],
    #   ["abcd", "ef"]
    # ]
    print(all_construct_tab_look_back("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    # []
    print(all_construct_tab_look_back("aaaaaaaaaz", ["a", "aa", "aaaa", "aaaaa", "aaaaaa"]))
    # []

    print()

    print(all_construct_tab_look_ahead("purple", ["purp", "p", "ur", "le", "purpl"]))
    # [
    #   ["purp", "le"],
    #   ["p", "ur", "p", "le"]
    # ]
    print(all_construct_tab_look_ahead("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    # [
    #   ["ab", "cd", "ef"],
    #   ["ab", "c", "def"],
    #   ["abc", "def"],
    #   ["abcd", "ef"]
    # ]
    print(all_construct_tab_look_ahead("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    # []
    print(all_construct_tab_look_ahead("aaaaaaaaaz", ["a", "aa", "aaaa", "aaaaa", "aaaaaa"]))
    # []
