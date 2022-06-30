from typing import List, Dict


def all_construct(target: str, word_list: List[str]) -> List[List[str]]:
    """
    Brute force solution – time = branching factor of tree ^ height of tree, space = height of tree
    Time: O(n^m)
    Space: O(m x n^m); in worst case, the final results array can have m elements where each element
        is an array of all (n^m) possible combinations
    """
    if target == "":
        return [[]]
    all_results = []
    for word in word_list:
        if target.startswith(word):
            results = all_construct(target[len(word):], word_list)
            all_results.extend(map(lambda result: [word] + result, results))
    return all_results


def all_construct_memo(target: str, word_list: List[str], memo: Dict[str, List[List[str]]]) -> List[List[str]]:
    """
    Memoized solution – time = num of nodes in the optimized tree, space = height of tree
    Time: O(n^m)
    Space: O(m x n^m); in worst case, the final results array can have m elements where each element
        is an array of all (n^m) possible combinations

    One thing to note here is that the memoized solution runs faster but for worst case, it runs at the same time and
    space complexity as the brute force version because we have to find all possible paths in the recursion tree.
    Worst case here would be, target = "aaaaaaaaaaaaaaaaa", word_list = ["a", "aa", "aaaa", "aaaaa", "aaaaaa"]
    """
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    all_results = []
    for word in word_list:
        if target.startswith(word):
            results = all_construct_memo(target[len(word):], word_list, memo)
            all_results.extend(map(lambda result: [word] + result, results))
    memo[target] = all_results
    return memo[target]


if __name__ == '__main__':
    # P2_1 in word-construct series
    # Given a target word and a list of words, return all the ways in which the target word can be constructed from the word list
    # The result should be a 2D array where each element inside the result should represent a combination that can construct target
    # Words in the word list can be reused
    # print(all_construct_memo("purple", ["purp", "p", "ur", "le", "purpl"], {}))
    # [
    #   ["purp", "le"],
    #   ["p", "ur", "p", "le"]
    # ]
    # print(all_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))
    # [
    #   ["ab", "cd", "ef"],
    #   ["ab", "c", "def"],
    #   ["abc", "def"],
    #   ["abcd", "ef"]
    # ]
    # print(all_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
    # []
    print(all_construct_memo("aaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaaa", "aaaaa", "aaaaaa"], {}))
    # []
