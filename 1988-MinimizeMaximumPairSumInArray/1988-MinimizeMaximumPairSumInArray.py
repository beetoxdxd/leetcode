# Last updated: 1/8/2026, 5:22:30 p.m.
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] > ans: ans = nums[i] + nums[j]
            i += 1
            j -= 1

        return ans