# Last updated: 1/11/2026, 7:13:50 p.m.
1class Solution:
2    def minMoves2(self, nums: list[int]) -> int:
3        nums.sort()
4        mediana = int(statistics.median(nums))
5        ans = 0
6
7        for num in nums:
8            ans += abs(mediana - num)
9
10        return ans