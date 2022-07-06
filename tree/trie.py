from __future__ import annotations

from typing import Dict, Union


class TrieNode:
    """
    An implementation of TrieNode using a Hashmap
    """
    def __init__(self):
        self._children: Dict[str, TrieNode] = {}
        self._is_word: bool = False

    @property
    def is_word(self) -> bool:
        return self._is_word

    @is_word.setter
    def is_word(self, value) -> None:
        self._is_word = value

    def has_child(self, char: str) -> bool:
        return char in self._children

    def get_child(self, char: str) -> TrieNode:
        return self._children[char]

    def add_child(self, char: str) -> None:
        self._children[char] = TrieNode()


class Trie:
    def __init__(self):
        self._root: TrieNode = TrieNode()

    def add(self, word: str) -> None:
        """
        Add a word to the Trie
        """
        if not word:
            return
        curr = self._root
        for char in word:
            if not curr.has_child(char):
                curr.add_child(char)
            curr = curr.get_child(char)
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Search for the existence of a word in the Trie
        """
        if not word:
            return False
        node: TrieNode = self.starts_with(word, get_node=True)
        return node is not None and node.is_word

    def starts_with(self, prefix: str, get_node: bool = False) -> Union[bool, TrieNode]:
        """
        Check is a string with matching prefix exists in the Trie
        If `get_node` is False - returns True if match found otherwise False
        If `get_node` is True - returns the TrieNode for to the last char in prefix if match found otherwise None
        """
        if not prefix:
            return None if get_node else False
        curr = self._root
        for char in prefix:
            if not curr.has_child(char):
                return None if get_node else False
            curr = curr.get_child(char)
        return curr if get_node else True


if __name__ == '__main__':
    trie = Trie()
    print("\nAdd 'apple'")
    trie.add("apple")

    print("\nAdd 'apples'")
    trie.add("apples")

    print("\nAdd 'applebees'")
    trie.add("applebees")

    print("\nSearch 'apple'")
    print(trie.search("apple"))  # should return True

    print("\nSearch 'app'")
    print(trie.search("app"))  # should return False

    print("\nPrefix check 'app'")
    print(trie.starts_with("app"))  # should return True
