# Last updated: 22/7/2026, 5:57:17 p.m.
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + val) % n] for i, val in enumerate(nums)]