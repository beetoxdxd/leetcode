# Last updated: 18/11/2026, 10:21:13 p.m.
1class Solution:
2    def minimizeSum(self, nums: List[int]) -> int:
3        nums.sort()
4
5        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])