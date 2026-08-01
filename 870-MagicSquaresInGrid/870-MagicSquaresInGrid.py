# Last updated: 1/8/2026, 5:25:45 p.m.
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def sum_matrix(m: int, n: int) -> bool:
            if grid[m+1][n+1] != 5: return False

            vals = [grid[m+i][n+j] for i in range(3) for j in range(3)]
            if len(set(vals)) != 9 or max(vals) > 9 or min(vals) < 1: return False

            if not all(sum(grid[m+i][n:n+3]) == 15 for i in range(3)): return False
            if not all(sum(grid[m+i][n+j] for i in range(3)) == 15 for j in range(3)): return False

            return True

        ans = 0
        if len(grid[0]) < 3 or len(grid) < 3: return ans
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if sum_matrix(i, j): ans += 1

        return ans