# Last updated: 1/8/2026, 5:28:52 p.m.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k, l, n = 0, 0, len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]: k = i

        for i in range(n):
            if nums[k] < nums[i]: l = i

        if k == l: 
            nums.sort()
            return
            
        nums[k], nums[l] = nums[l], nums[k]
        k, l = k+1, n-1
        
        while k < l:
            nums[k], nums[l] = nums[l], nums[k]
            k += 1
            l -= 1
