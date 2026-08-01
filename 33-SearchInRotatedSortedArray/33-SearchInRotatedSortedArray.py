# Last updated: 1/8/2026, 5:28:47 p.m.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            h = (i+j) // 2

            if nums[h] == target: return h
            if nums[i] <= nums[h]: # ordenado
                if nums[i] <= target <= nums[h]: j = h-1
                else: i = h+1
            else:
                if nums[h] <= target <= nums[j]: i = h+1
                else: j = h-1

        return -1