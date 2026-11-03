# Last updated: 2/11/2026, 11:25:18 p.m.
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        mx = max(nums)
4        ans = 0
5
6        for num in nums:
7            ans += mx - num
8
9        return ans