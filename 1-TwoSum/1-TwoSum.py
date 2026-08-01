# Last updated: 1/8/2026, 5:29:46 p.m.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target: return [i,j]