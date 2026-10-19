# Last updated: 18/10/2026, 10:45:27 p.m.
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        ans = []
4
5        for i, num in enumerate(sorted(nums)):
6            if num == target: ans.append(i)
7
8        return ans
9