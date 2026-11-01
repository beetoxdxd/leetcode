# Last updated: 1/11/2026, 1:30:01 a.m.
class Solution:
    def minMoves(self, nums):
        return sum(nums) - min(nums) * len(nums)