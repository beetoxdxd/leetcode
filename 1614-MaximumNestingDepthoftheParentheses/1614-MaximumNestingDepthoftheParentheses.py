# Last updated: 27/9/2026, 6:33:35 p.m.
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        par = 0
4        ans = 0
5
6        for char in s:
7            if char == '(': par += 1
8            elif char == ')': par -= 1
9
10            ans = max(ans, par)
11
12        return ans