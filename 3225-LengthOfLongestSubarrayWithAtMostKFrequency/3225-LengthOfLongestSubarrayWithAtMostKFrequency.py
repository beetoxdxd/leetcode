# Last updated: 27/8/2026, 4:59:12 p.m.
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        j = 0
        h = {}
        ans = 0

        for i, num in enumerate(nums):
            if num not in h: h[num] = k

            ans = max(ans, i-j)
            while j < i and h[num] == 0:
                h[nums[j]] += 1
                j += 1

            h[num] -= 1

        return max(ans, i+1-j)