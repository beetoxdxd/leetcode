# Last updated: 1/8/2026, 5:27:29 p.m.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        l = len(nums)//2
        if l == 0: return nums[0]
        for num in nums:
            if not num in h: h[num] = 1
            elif h[num] > l: return num
            h[num] += 1