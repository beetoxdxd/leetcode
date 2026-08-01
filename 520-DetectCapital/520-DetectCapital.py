# Last updated: 1/8/2026, 5:26:41 p.m.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lower = 0
        n = len(word)

        for char in word:
            if char.islower(): lower += 1
            else: upper += 1

        if lower == n: return True
        if upper == n: return True
        return word[0].isupper() and lower == n-1