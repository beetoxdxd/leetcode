# Last updated: 1/11/2026, 1:27:39 a.m.
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        mn, mx = min(nums), max(nums)
4        if mn == mx: return 0
5
6        ans = 0
7
8        for num in nums:
9            ans += num - mn
10
11        return ans