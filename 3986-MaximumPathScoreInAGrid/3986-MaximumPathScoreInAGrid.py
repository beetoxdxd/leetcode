# Last updated: 22/7/2026, 5:56:31 p.m.
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1 for _ in range(k+1)] for _ in range(n+1)] for _ in range(m+1)]
        c = 0 if grid[0][0] == 0 else 1
        if c > k: return -1
        dp[1][1][c] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue

                if grid[i][j] == 0: cost = 0
                else: cost = 1

                for c in range(k+1):
                    if c < cost or (dp[i][j+1][c-cost] == -1 and dp[i+1][j][c-cost] == -1): continue
                    dp[i+1][j+1][c] = max(dp[i][j+1][c-cost], dp[i+1][j][c-cost]) + grid[i][j]

        return max(dp[-1][-1])