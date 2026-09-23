# Last updated: 22/9/2026, 11:36:39 p.m.
1class Solution:
2    def numTrees(self, n: int) -> int:
3
4        @cache
5        def traverse(x: int) -> int:
6            if x == 1 or x == 0: return 1
7
8            total = 0
9            for i in range(x):
10                total += traverse(i) * traverse(x-i-1)
11
12            return total
13
14        return traverse(n)