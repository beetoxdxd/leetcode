# Last updated: 1/8/2026, 5:22:48 p.m.
class Solution:
    def check(self, nums: List[int]) -> bool:
        max1, min1 = nums[0], nums[0]
        i = 1
        n = len(nums)
        
        while i < n and nums[i] >= nums[i-1]:
            max1 = max(max1, nums[i])
            min1 = min(min1, nums[i])
            i += 1
            
        if i == n: return True
        max2, min2 = nums[i], nums[i]
        i += 1
        
        while i < n and nums[i] >= nums[i-1]:
            max2 = max(max2, nums[i])
            min2 = min(min2, nums[i])
            i += 1
            
        return i == n and min2 <= max2 <= min1 <= max1
        
        