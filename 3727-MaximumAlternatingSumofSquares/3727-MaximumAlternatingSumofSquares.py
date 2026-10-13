# Last updated: 13/10/2026, 4:43:56 p.m.
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        nums = sorted(abs(num) for num in nums)
5        ans = 0
6        
7        for i in range(n//2):
8            ans -= nums[i]**2
9
10        for i in range(n//2, n):
11            ans += nums[i]**2
12
13        return ans