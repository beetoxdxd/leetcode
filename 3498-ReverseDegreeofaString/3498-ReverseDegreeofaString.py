# Last updated: 19/9/2026, 6:57:08 p.m.
1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        value = [26 - i for i in range(26)]
4        return sum(value[ord(char) - 97] * (i+1) for i, char in enumerate(s))