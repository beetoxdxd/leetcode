# Last updated: 22/7/2026, 5:56:28 p.m.
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k*(max(nums) - min(nums))