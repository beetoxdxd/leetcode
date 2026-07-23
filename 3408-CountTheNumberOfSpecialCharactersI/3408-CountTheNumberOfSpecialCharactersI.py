# Last updated: 22/7/2026, 11:35:18 p.m.
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()
        ans = 0

        for char in word:
            if 'a' <= char <= 'z' and char not in lower:
                lower.add(char)
                if char.upper() in upper: ans += 1

            if 'A' <= char <= 'Z' and char not in upper:
                upper.add(char)
                if char.lower() in lower: ans += 1

        return ans