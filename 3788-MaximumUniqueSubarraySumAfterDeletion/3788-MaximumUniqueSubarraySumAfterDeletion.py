# Last updated: 22/7/2026, 5:57:02 p.m.
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0

        for num in list(set(nums)):
            if num >= 0: ans += num

        return ans if ans > 0 else max(nums)