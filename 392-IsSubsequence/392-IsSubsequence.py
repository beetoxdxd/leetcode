# Last updated: 1/8/2026, 5:26:59 p.m.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in t:
            if j >= len(s): return True
            if i == s[j]:
                j += 1

        if j == len(s): return True
        return False 