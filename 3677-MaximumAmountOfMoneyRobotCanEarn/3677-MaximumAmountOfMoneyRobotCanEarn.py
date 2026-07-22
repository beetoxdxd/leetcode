# Last updated: 22/7/2026, 5:57:15 p.m.
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        dp = [[[-math.inf]*3 for i in range(n+1)] for _ in range(m+1)]
        dp[1][0] = dp[0][1] = [0,0,0]

        for i in range(m):
            for j in range(n):
                current = coins[i][j]
                for k in range(3):
                    if k == 0:
                        dp[i+1][j+1][k] = max(dp[i][j+1][k] + current, dp[i+1][j][k] + current)
                    else:
                        dp[i+1][j+1][k] = max(dp[i][j+1][k] + current, dp[i+1][j][k] + current, dp[i][j+1][k-1], dp[i+1][j][k-1])

        return max(dp[-1][-1])