# Last updated: 22/7/2026, 11:35:47 p.m.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(1) > 0: return n - nums.count(1)
        res = math.inf
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = math.gcd(g, nums[j])
                if g == 1: res = min(res, j-i)

        return -1 if res == math.inf else res + n -1