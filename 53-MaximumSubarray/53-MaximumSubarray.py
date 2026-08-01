# Last updated: 1/8/2026, 5:28:20 p.m.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ, prev = nums[0], -math.inf

        for i in range(1, len(nums)):
            if summ < 0 and nums[i] > summ: summ = nums[i]
            elif summ + nums[i] <= 0: 
                if prev < summ: prev = summ
                summ = nums[i]
            else: 
                if nums[i] < 0 and prev < summ: prev = summ
                summ += nums[i]

        return summ if summ > prev else prev