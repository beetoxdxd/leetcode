# Last updated: 1/8/2026, 5:24:31 p.m.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        size = m*n
        k = size - (k % size)        

        if k == size or k == 0: return grid

        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = grid[k//n][k%n]
                k = (k+1) % size

        return ans