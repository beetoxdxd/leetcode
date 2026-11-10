# Last updated: 9/11/2026, 11:50:21 p.m.
1class Solution:
2    def climbStairs(self, n: int, costs: List[int]) -> int:
3        dp = [math.inf] * n
4        prev = 0
5        for i in range(n):
6
7            dp[i] = min(dp[i], prev + costs[i] + 1)
8            if i + 1 < n: dp[i+1] = min(dp[i+1], prev + costs[i+1] + 4)
9            if i + 2 < n: dp[i+2] = min(dp[i+2], prev + costs[i+2] + 9)
10
11            prev = dp[i]
12
13        return dp[-1]