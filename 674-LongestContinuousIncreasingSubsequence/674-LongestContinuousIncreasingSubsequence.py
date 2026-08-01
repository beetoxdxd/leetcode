# Last updated: 1/8/2026, 5:26:23 p.m.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        cont = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: cont += 1
            else: cont = 1

            ans = max(ans, cont)

        return ans