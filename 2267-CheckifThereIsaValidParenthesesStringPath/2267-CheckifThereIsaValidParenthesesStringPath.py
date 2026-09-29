# Last updated: 28/9/2026, 11:00:57 p.m.
1class Solution:
2    def hasValidPath(self, grid: list[list[str]]) -> bool:
3        n = len(grid)
4        m = len(grid[0])
5        path_len = n + m - 1
6
7        if path_len % 2 == 1:
8            return False
9        if grid[0][0] != "(" or grid[n - 1][m - 1] != ")":
10            return False
11
12        dp = [[0] * m for _ in range(n)]
13
14        dp[0][0] = 1 << 1
15
16        for i in range(n):
17            for j in range(m):
18                change = 1 if grid[i][j] == "(" else -1
19
20                if i > 0:
21                    if change == 1:
22                        dp[i][j] |= dp[i - 1][j] << 1
23                    else:
24                        dp[i][j] |= dp[i - 1][j] >> 1
25
26                if j > 0:
27                    if change == 1:
28                        dp[i][j] |= dp[i][j - 1] << 1
29                    else:
30                        dp[i][j] |= dp[i][j - 1] >> 1
31
32        return bool(dp[n - 1][m - 1] & 1)