# Last updated: 1/8/2026, 5:26:57 p.m.
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        i = 0
        prev = 0

        for num in nums:
            prev += i*num
            i += 1

        ans = prev
        for i in range(n-1, 0, -1):
            prev += total - n*nums[i]
            ans = max(ans, prev)

        return ans