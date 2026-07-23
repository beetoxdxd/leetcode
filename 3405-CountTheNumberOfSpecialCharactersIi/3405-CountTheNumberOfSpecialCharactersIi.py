# Last updated: 22/7/2026, 11:35:21 p.m.
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lo, up = [False] * 26, [False] * 26
        for ch in word:
            if ch.islower():
                lo[ord(ch) - ord('a')] = not up[ord(ch) - ord('a')]
            else:
                up[ord(ch) - ord('A')] = True
        return sum([a and b for a, b in zip(lo, up)])