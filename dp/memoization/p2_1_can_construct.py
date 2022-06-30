from typing import List, Dict


def can_construct(target: str, word_list: List[str]) -> bool:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    If `n` is the length of word list and `m` is the length of the target word
    Time: O(n^m x m); the extra O(m) is for prefix checking + slicing inside the loop
    Space: O(m^2); stack depth is O(m) and within every frame, we slice the word to pass in suffix which takes O(m)
        additional space
    """
    if target == "":
        return True
    for word in word_list:
        if target.startswith(word):
            if can_construct(target[len(word):], word_list):
                return True
    return False


def can_construct_memo(target: str, word_list: List[str], memo: Dict[str, bool]) -> bool:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    If `n` is the length of word list and `m` is the length of the target word
    Time: O(m^2 x n); in worst case, for every character in target word, we have to look at the entire word list
        (so O(m x n)) and apart from that, the extra O(m) is for prefix checking + slicing inside the loop
    Space: O(m^2); stack depth is O(m) and within every frame, we slice the word to pass in suffix which takes O(m)
        additional space so total O(m^2) so far; apart from that, we need to keep in worst case we might need to keep
        track of every possible substring of target word (depending on th word list of course), so that's O(m^2)
        because there can be at most m^2 substrings inside a string of length m; so grand total is O(2 x m^2)
    """
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in word_list:
        if target.startswith(word):
            result = can_construct_memo(target[len(word):], word_list, memo)
            if result:
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]


if __name__ == '__main__':
    # P2_1 in word-construct series
    # Given a target word and a list of words, check if target word can be constructed from the word list
    # Words in the word list can be reused
    print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))  # true
    print(can_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))  # false
    print(can_construct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))  # true
    print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eee", "eeee", "eeeee", "eeeeeee"], {}))  # false (there is no 'f' in the list)
