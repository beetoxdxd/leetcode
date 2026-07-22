# Last updated: 22/7/2026, 5:56:36 p.m.
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t = x+k-1
        for i in range(x, x + k//2):
            for j in range(y, y+k):
                grid[i][j], grid[t][j] = grid[t][j], grid[i][j]
            t -= 1

        return grid
