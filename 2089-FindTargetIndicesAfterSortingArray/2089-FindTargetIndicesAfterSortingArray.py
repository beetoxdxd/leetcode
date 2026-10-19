# Last updated: 18/10/2026, 10:47:39 p.m.
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        return [i for i, num in enumerate(sorted(nums)) if num == target]