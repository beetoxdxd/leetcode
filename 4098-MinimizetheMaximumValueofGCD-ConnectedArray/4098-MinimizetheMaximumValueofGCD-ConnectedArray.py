# Last updated: 2/11/2026, 3:48:45 p.m.
1class Solution:
2    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
3        p = value
4        for i in range(2, math.isqrt(value) + 1):
5            if value % i != 0: continue
6            p = i
7            break 
8
9        left = value - p if index > 0 else value
10        if left != value: left -= 2*(index-1)
11
12        if left <= 1: return -1
13        right = value + p if index < n-1 else value
14
15        if right == value: return right
16        return 2*(n-index-2) + right