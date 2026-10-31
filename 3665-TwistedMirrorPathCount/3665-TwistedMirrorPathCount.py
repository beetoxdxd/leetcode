# Last updated: 31/10/2026, 5:27:03 p.m.
1mat = [[[1, 1], [1, 1]], [[0, 1], [1, 0]]]
2MOD = 10**9 + 7
3
4class Solution:
5    def uniquePaths(self, A: List[List[int]]) -> int:
6        n, left = len(A[0]), 0
7        dp = [0] * n
8
9        dp[0] = 1
10
11        for row in A:
12            left = 0
13            for j, c in enumerate(row):
14                top = dp[j]
15
16                dp[j] = (left * mat[c][1][0] + top * mat[c][1][1]) % MOD
17                left  = (left * mat[c][0][0] + top * mat[c][0][1]) % MOD
18
19        return left