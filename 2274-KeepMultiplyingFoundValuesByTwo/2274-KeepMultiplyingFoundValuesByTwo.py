# Last updated: 22/7/2026, 11:36:10 p.m.
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2

        return original