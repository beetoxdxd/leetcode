# Last updated: 19/9/2026, 10:22:31 p.m.
1class Solution:
2    def trap(self, height: list[int]) -> int:
3        max_left = 0
4        max_right = 0
5        n = len(height)
6        i, j = 0, n-1
7        dp = [math.inf] * n
8
9        while i < n:
10            if height[i] > max_left: max_left = height[i]
11            if height[j] > max_right: max_right = height[j]
12
13            dp[i] = min(max_left - height[i], dp[i])
14            dp[j] = min(max_right - height[j], dp[j])
15
16            i += 1
17            j -= 1
18
19        return sum(dp)