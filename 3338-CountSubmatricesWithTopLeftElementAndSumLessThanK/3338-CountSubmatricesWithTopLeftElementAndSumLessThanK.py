# Last updated: 22/7/2026, 11:35:23 p.m.
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[0] * (n+1) for _ in range(m+1)]
        ans = 0

        for i in range(m):
            for j in range(n):
                matrix[i+1][j+1] = grid[i][j] + matrix[i][j+1] + matrix[i+1][j] - matrix[i][j]

                if matrix[i+1][j+1] <= k: ans += 1
                else: break

        return ans