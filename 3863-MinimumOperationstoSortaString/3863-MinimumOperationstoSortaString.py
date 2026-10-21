# Last updated: 20/10/2026, 11:49:21 p.m.
1class Solution:
2    def minOperations(self, s: str) -> int:
3        n = len(s)
4        if all(s[i] <= s[i+1] for i in range(n - 1)): return 0
5        if n == 2: return -1
6
7        mn, mx = min(s), max(s)
8        if mn == s[0] or mx == s[-1]: return 1
9        if any(ch == mn or ch == mx for ch in s[1:-1]): return 2
10        return 3