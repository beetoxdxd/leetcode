# Last updated: 1/8/2026, 5:26:20 p.m.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cont, ans, prev = 1, 0, 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]: cont += 1
            else: 
                ans += min(cont, prev)
                prev, cont = cont, 1

        ans += min(cont, prev)
        return ans