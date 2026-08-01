# Last updated: 1/8/2026, 5:29:22 p.m.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
        current.is_end_of_word = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for string in strs:
            trie.insert(string)

        current = trie.root
        prefix = []

        while len(current.children) == 1 and not current.is_end_of_word:
            char = list(current.children.keys())[0]
            prefix.append(char)
            current = current.children[char]

        return ''.join(prefix)