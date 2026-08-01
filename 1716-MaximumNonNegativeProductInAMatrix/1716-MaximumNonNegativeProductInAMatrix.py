# Last updated: 1/8/2026, 5:23:24 p.m.
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [[grid[0][i], grid[0][i]] for i in range(n)] # [min, max]

        for i in range(1, n):
            row[i][0] *= row[i-1][0]
            row[i][1] = row[i][0]

        for i in range(1, m):
            row[0][0] *= grid[i][0]
            row[0][1] = row[0][0]

            for j in range(1, n):
                op = [(grid[i][j] * num) for k in range(j-1, j+1) for num in row[k]]
                row[j] = [min(op), max(op)]

        return -1 if row[n-1][1] < 0 else row[n-1][1] % (10**9 + 7)
