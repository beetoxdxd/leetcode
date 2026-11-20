# Last updated: 19/11/2026, 8:16:58 p.m.
1class Solution:
2    def maxSelectedElements(self, nums: List[int]) -> int:
3        nums.sort()
4        dp = {}
5        ans = 0
6        for x in nums:
7            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)
8            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)
9            ans = max(ans, dp[x], dp[x + 1])
10        return ans