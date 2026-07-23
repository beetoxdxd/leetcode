# Last updated: 22/7/2026, 11:35:22 p.m.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, i: int, words_container: List[str]) -> None:
        current = self.root

        def update_best(node):
            if node.best_index == -1: node.best_index = i
            else:
                if len(words_container[i]) < len(words_container[node.best_index]): node.best_index = i
        
        update_best(current)

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
            update_best(current)

        current.is_end_of_word = True

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()

        for i, word in enumerate(wordsContainer):
            trie.insert(word[::-1], i, wordsContainer)

        ans = []
        for word in wordsQuery:
            word = word[::-1]
            current = trie.root

            for char in word:
                if char not in current.children: break
                current = current.children[char]

            ans.append(current.best_index)
        return ans