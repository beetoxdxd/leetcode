# Last updated: 1/8/2026, 5:27:38 p.m.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        ans = nums[0]

        while i < j:
            h = (i+j) // 2
            ans = min(ans, nums[h], nums[i], nums[j])

            if nums[i] < nums[h]: i = h+1
            else: j = h-1

        return ans