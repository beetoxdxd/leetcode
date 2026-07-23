# Last updated: 22/7/2026, 11:35:41 p.m.
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n+1: return False

        nums.sort()
        i = 1

        for i in range(1, n+1):
            if nums[i-1] != i: return False

        return nums[-1] == n