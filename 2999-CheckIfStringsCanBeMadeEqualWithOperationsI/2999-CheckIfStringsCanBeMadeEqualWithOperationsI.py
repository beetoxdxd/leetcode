# Last updated: 22/7/2026, 11:35:37 p.m.
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(2):
            if (s1[i] != s2[i+2] or s1[i+2] != s2[i]) and (s1[i] != s2[i] or s1[i+2] != s2[i+2]): return False

        return True