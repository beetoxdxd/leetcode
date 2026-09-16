# Last updated: 16/9/2026, 2:46:27 a.m.
1class Solution:
2    def numberOfSets(self, n: int, k: int) -> int:
3        dp = [[0] * (n) for _ in range(k)]
4
5        for i in range(1, n+1):
6            dp[0][i-1] = (i)*(i-1) // 2
7
8        if k == 1: return dp[-1][-1] % (10**9 + 7)
9
10        for i in range(1, n): # prefix sum
11            dp[0][i] += dp[0][i-1]
12
13        for i in range(2, n):
14            x = i - 1
15            dp[1][i] = (x)*(x+1) // 2 + dp[0][x-1] + dp[1][i-1]
16
17        if k == 2: return dp[-1][-1] % (10**9 + 7)
18        
19        for i in range(2, k):
20            for j in range(1, n): # prefix sum
21                dp[i-1][j] += dp[i-1][j-1]
22
23            for j in range(i+1, n):
24                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
25
26        return dp[-1][-1] % (10**9 + 7)