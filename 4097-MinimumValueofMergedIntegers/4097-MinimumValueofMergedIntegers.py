# Last updated: 2/11/2026, 12:26:06 a.m.
1class Solution:
2    def minMergedInteger(self, nums: list[int]) -> int:
3        ans = math.inf
4        for i in range(0, len(nums), 2):
5            ans = min(ans, nums[i] * (10**len(str(nums[i+1]))) + nums[i+1])
6
7        return ans