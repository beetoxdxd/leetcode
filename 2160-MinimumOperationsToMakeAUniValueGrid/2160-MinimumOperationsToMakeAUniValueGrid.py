# Last updated: 1/8/2026, 5:22:05 p.m.
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        row = [item for r in grid for item in r]
        n = len(row)
        row.sort()
        med = row[(n-1)//2]
        ans = 0

        for item in row:
            div = abs(item-med)
            if div % x != 0: return -1

            ans += abs(item-med) // x

        return ans