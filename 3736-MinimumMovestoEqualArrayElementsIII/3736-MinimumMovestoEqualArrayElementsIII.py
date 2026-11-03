# Last updated: 2/11/2026, 11:27:10 p.m.
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        return len(nums) * max(nums) - sum(nums)