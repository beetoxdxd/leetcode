# Last updated: 16/9/2026, 11:36:44 p.m.
1class Solution:
2    def minSumOfLengths(self, arr: List[int], target: int) -> int:
3        n, ans, total = len(arr), len(arr) + 1, 0
4        dp = [n] * (n + 1)
5        left = 0
6        for right, x in enumerate(arr):
7            total += x
8            while total > target:
9                total -= arr[left]
10                left += 1
11            dp[right + 1] = dp[right]
12            if total == target:
13                ans = min(ans, right - left + 1 + dp[left])
14                dp[right + 1] = min(dp[right], right - left + 1)
15        return -1 if ans == n + 1 else ans