# Last updated: 22/7/2026, 11:35:43 p.m.
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n

        for j in range(n):
            for i in range(j):
                if -target <= nums[j] - nums[i] <= target:
                    if i > 0 and dp[i] == 0: continue
                    dp[j] = max(dp[j], dp[i]+1)

        return dp[-1] if dp[-1] > 0 else -1