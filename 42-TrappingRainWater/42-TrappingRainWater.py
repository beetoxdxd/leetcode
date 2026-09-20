# Last updated: 19/9/2026, 10:25:09 p.m.
1class Solution:
2    def trap(self, height: list[int]) -> int:
3        n = len(height)
4        dp = [math.inf] * n
5        max_left, max_right = 0, 0
6
7        for i in range(n):
8            if height[i] > max_left: max_left = height[i]
9            if height[-i-1] > max_right: max_right = height[-i-1]
10
11            dp[i] = min(max_left - height[i], dp[i])
12            dp[-i-1] = min(max_right - height[-i-1], dp[-i-1])
13
14        return sum(dp)