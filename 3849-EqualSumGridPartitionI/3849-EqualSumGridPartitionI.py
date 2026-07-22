# Last updated: 22/7/2026, 5:56:55 p.m.
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sums = [sum(row) for row in grid]
        total = sum(row_sums)

        if total % 2 != 0: return False

        target = total // 2
        section = 0
        for i in range(m-1):
            section += row_sums[i]

            if section == target: return True

        col = 0
        for j in range(n-1):
            for i in range(m):
                col += grid[i][j]

            if col == target: return True

        return False