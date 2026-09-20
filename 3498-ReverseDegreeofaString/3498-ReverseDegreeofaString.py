# Last updated: 19/9/2026, 7:20:39 p.m.
1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        return sum((123 - ord(char)) * (i+1) for i, char in enumerate(s))