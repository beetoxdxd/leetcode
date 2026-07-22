# Last updated: 22/7/2026, 5:57:11 p.m.
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ans = 0
        aux = []

        for i, row in enumerate(grid):
            row.sort(reverse=True)

            aux.extend(row[:limits[i]])

        ans = 0
        aux.sort()

        for i in range(k):
            ans += aux.pop()

        return ans