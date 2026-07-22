# Last updated: 22/7/2026, 5:56:41 p.m.
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        i, j, n = 0, 1, len(nums)

        while j < n:
            if nums[j] <= nums[i]*k: j += 1
            else: i += 1

            ans = max(ans, j-i)
        return n-ans