# Last updated: 22/7/2026, 5:56:11 p.m.
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        abc = 'abcdefghijklmnopqrstuvwxyz'[::-1]

        ans = []
        for word in words:
            weight = 0

            for char in word:
                weight += weights[ord(char) - ord('a')]

            ans.append(abc[weight % 26])

        return ''.join(ans)