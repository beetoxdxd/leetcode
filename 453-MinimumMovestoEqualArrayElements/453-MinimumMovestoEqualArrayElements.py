# Last updated: 1/11/2026, 1:20:15 a.m.
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        mn = min(nums)
4        ans = 0
5
6        for num in nums:
7            if mn != num: 
8                ans += num - mn
9
10        return ans