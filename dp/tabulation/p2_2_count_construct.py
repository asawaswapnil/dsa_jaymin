from typing import List


def count_construct_tab_look_back(target: str, word_list: List[str]) -> int:
    """
    Tabulated solution
    Time: O(m^2 x n)
    Space: O(m)
    """
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for end_idx in range(1, len(table)):
        target_sub_str = target[:end_idx]
        for word in word_list:
            if len(word) <= len(target_sub_str):
                if table[end_idx - len(word)] > 0 and target_sub_str.endswith(word):
                    table[end_idx] += table[end_idx - len(word)]
    return table[len(target)]


def count_construct_tab_look_ahead(target: str, word_list: List[str]) -> int:
    """
    Tabulated solution
    Time: O(m^2 x n)
    Space: O(m^2)
    """
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for end_idx in range(len(table)):
        if table[end_idx] > 0:
            target_sub_str = target[end_idx:]
            for word in word_list:
                if len(word) <= len(target_sub_str):
                    if target_sub_str.startswith(word):
                        table[end_idx + len(word)] += table[end_idx]
    return table[len(target)]


if __name__ == '__main__':
    # P2_2 in word-construct series
    # Given a target word and a list of words, return total number of ways in which the target word can be constructed from the word list
    # Words in the word list can be reused
    print(count_construct_tab_look_back("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    print(count_construct_tab_look_back("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(count_construct_tab_look_back("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(count_construct_tab_look_back("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(count_construct_tab_look_back("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"]))  # 0 (there is no 'f' in the list)
    print(count_construct_tab_look_back("eeef", ["e", "eee", "f", "eeef"]))  # 3
    print()
    print(count_construct_tab_look_ahead("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    print(count_construct_tab_look_ahead("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(count_construct_tab_look_ahead("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(count_construct_tab_look_ahead("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(count_construct_tab_look_ahead("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"]))  # 0 (there is no 'f' in the list)
    print(count_construct_tab_look_ahead("eeef", ["e", "eee", "f", "eeef"]))  # 3
