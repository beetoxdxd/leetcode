# Last updated: 18/10/2026, 10:54:45 p.m.
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        index, cont = 0, 0
4
5        for num in nums:
6            if num < target: index += 1
7            elif num == target: cont += 1
8
9        return [i for i in range(index, index+cont)]