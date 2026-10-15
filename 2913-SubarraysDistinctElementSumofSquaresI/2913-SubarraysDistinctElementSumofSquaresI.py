# Last updated: 14/10/2026, 11:10:09 p.m.
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        n = len(nums)
4        ans = 0
5
6        for i in range(n):
7            distinct = set()
8            for j in range(i, n):
9                distinct.add(nums[j])
10
11                ans += len(distinct)**2
12
13        return ans