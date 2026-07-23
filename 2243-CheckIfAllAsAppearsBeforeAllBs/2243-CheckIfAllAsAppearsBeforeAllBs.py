# Last updated: 22/7/2026, 11:36:15 p.m.
class Solution:
    def checkString(self, s: str) -> bool:
        a, b = -math.inf, math.inf

        for i,char in enumerate(s):
            if b < a: return False
            a = i if char == 'a' else a
            b = i if char == 'b' else b

        return a < b