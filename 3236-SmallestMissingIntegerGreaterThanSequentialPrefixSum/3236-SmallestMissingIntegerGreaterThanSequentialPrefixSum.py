# Last updated: 27/8/2026, 4:59:09 p.m.
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        summ = nums[0]
        j = 1

        while j < n and nums[j] == nums[j-1] + 1:
            summ += nums[j]
            j += 1

        aux = set(nums)
        while summ in aux: summ += 1

        return summ