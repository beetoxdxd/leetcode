# Last updated: 2/11/2026, 11:28:18 p.m.
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        n, mx, sm = 0, 0, 0
4        for num in nums:
5            n += 1
6            mx = max(mx, num)
7            sm += num
8            
9        return n * mx - sm