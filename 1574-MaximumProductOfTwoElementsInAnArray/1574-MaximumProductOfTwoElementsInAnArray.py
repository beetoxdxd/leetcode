# Last updated: 1/8/2026, 5:23:44 p.m.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)