from typing import List


def can_construct_tab_look_back(target: str, word_list: List[str]) -> bool:
    """
    Tabulated solution
    If `n` is the length of word list and `m` is the length of the target word
    Time: O(m^2 x n)
    Space: O(m)
    """
    table = [False for _ in range(len(target) + 1)]
    table[0] = True  # base case

    for end_idx in range(1, len(table)):
        target_sub_str = target[:end_idx]
        for word in word_list:
            # can I make the new target word (target_sub_str) ending in current end_idx from list of words
            if len(word) <= len(target_sub_str):
                if table[end_idx - len(word)] and target_sub_str.endswith(word):
                    table[end_idx] = True
                    break
    return table[len(target)]


def can_construct_tab_look_ahead(target: str, word_list: List[str]) -> bool:
    """
    Tabulated solution
    If `n` is the length of word list and `m` is the length of the target word
    Time: O(m^2 x n)
    Space: O(m)
    """
    table = [False for _ in range(len(target) + 1)]
    table[0] = True  # base case

    for end_idx in range(len(table)):
        if table[end_idx]:
            # I can make the word ending at current end_idx
            target_sub_str = target[end_idx:]
            for word in word_list:
                # what other words I can make in the remaining part of the target word (target_sub_str)
                if len(word) <= len(target_sub_str):
                    if target_sub_str.startswith(word):
                        table[end_idx + len(word)] = True
    return table[len(target)]


def can_construct_tab_optimized(target: str, word_list: List[str]) -> bool:
    """
    Optimized version which used converts all strings to their memory views which reduces
    the time taken while slicing the strings. Slicing a string is basically creating a copy
    which is O(n) but using Python's memoryview we can avoid copying strings while slicing them
    If `n` is the length of word list and `m` is the length of the target word
    Time: ~O(m x n); the extra O(m) for slicing and copying is now O(1) with the memory views
    Space: O(m)
    """
    target = memoryview(target.encode('utf-8'))
    word_list = [memoryview(word.encode('utf-8')) for word in word_list]

    table = [False for _ in range(len(target) + 1)]
    table[0] = True  # base case

    for end_idx in range(len(table)):
        if table[end_idx]:
            # I can make the word ending at current end_idx
            target_sub_str = target[end_idx:]
            for word in word_list:
                # what other words I can make in the remaining part of the target word (target_sub_str)
                if len(word) <= len(target_sub_str):
                    if target_sub_str[:len(word)] == word:
                        table[end_idx + len(word)] = True
    return table[len(target)]


if __name__ == '__main__':
    # P2_1 in word-construct series
    # Given a target word and a list of words, check if target word can be constructed from the word list
    # Words in the word list can be reused
    print(can_construct_tab_look_back("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(can_construct_tab_look_back("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
    print(can_construct_tab_look_back("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # true
    print(can_construct_tab_look_back("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"]))  # false (there is no 'f' in the list)
    print()
    print(can_construct_tab_look_ahead("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(can_construct_tab_look_ahead("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
    print(can_construct_tab_look_ahead("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # true
    print(can_construct_tab_look_ahead("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"]))  # false (there is no 'f' in the list)
    print()
    print(can_construct_tab_optimized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(can_construct_tab_optimized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
    print(can_construct_tab_optimized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # true
    print(can_construct_tab_optimized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"]))  # false (there is no 'f' in the list)
