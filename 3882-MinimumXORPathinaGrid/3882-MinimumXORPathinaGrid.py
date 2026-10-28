# Last updated: 27/10/2026, 11:05:52 p.m.
1class Solution:
2    def minCost(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        dp = [[set() for j in range(n)] for i in range(m)]
5        dp[0][0].add(grid[0][0])
6
7        for i in range(1, n):
8            dp[0][i].update(grid[0][i] ^ val for val in dp[0][i-1])
9
10        for i in range(1, m):
11            dp[i][0].update(grid[i][0] ^ val for val in dp[i-1][0])
12
13        for i in range(1, m):
14            for j in range(1, n):
15                dp[i][j].update(grid[i][j] ^ val for val in dp[i-1][j])
16                dp[i][j].update(grid[i][j] ^ val for val in dp[i][j-1])
17
18        return min(dp[-1][-1])