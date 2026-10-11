# Last updated: 11/10/2026, 3:15:56 p.m.
1class Solution:
2    def sumOfSquares(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        return sum(0 if n%(i+1) else num**2 for i, num in enumerate(nums))