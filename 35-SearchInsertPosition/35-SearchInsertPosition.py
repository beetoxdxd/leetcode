# Last updated: 1/8/2026, 5:28:45 p.m.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        index = 0

        while i <= j:
            h = (i+j)//2

            if nums[h] == target: return h
            elif nums[h] > target: j = h-1
            else: 
                i = h+1
                index = i

        return index