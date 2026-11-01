# Last updated: 1/11/2026, 1:19:30 a.m.
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        nums.sort()
4        ans = 0
5
6        for i in range(len(nums) - 1, -1, -1):
7            diff = nums[i] - nums[0]
8            ans += diff
9
10        return ans