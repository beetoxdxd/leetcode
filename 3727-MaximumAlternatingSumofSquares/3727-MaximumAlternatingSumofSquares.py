# Last updated: 13/10/2026, 4:44:48 p.m.
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        for i in range(n):
5            nums[i] *= nums[i]
6        nums.sort()
7        return -sum(nums[: n // 2]) + sum(nums[n // 2 :])