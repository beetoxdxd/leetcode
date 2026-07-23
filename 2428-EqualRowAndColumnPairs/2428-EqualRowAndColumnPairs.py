# Last updated: 22/7/2026, 11:36:04 p.m.
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        cont = 0
        h = {}

        for row in grid:
            if str(row) in h: h[str(row)] += 1
            else: h[str(row)] = 1

        for j in range(size):
            col = [grid[i][j] for i in range(size)]
            if str(col) in h: cont += h[str(col)]
        return cont