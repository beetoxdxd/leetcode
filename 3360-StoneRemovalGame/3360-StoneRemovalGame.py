# Last updated: 25/11/2026, 11:31:19 p.m.
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        
4        for i in range(10, 0, -1):
5            n -= i
6            if n >= 0: continue
7
8            return i % 2 != 0