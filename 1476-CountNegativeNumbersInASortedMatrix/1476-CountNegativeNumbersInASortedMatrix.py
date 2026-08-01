# Last updated: 1/8/2026, 5:24:07 p.m.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid) - 1
        n = len(grid[0])
        j = 0

        while m >= 0 and j < n:
            if grid[m][j] < 0:
                ans += n - j
                m -= 1
            else:
                j += 1
        
        return ans
