# Last updated: 7/8/2026, 5:46:44 p.m.
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, (nums[i] * nums[j]) // pow(math.gcd(nums[i], nums[j]), 2))

        return ans