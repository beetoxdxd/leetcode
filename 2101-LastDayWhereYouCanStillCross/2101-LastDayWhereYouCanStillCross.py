# Last updated: 1/8/2026, 5:22:13 p.m.
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = [i for i in range(row*col + 2)]
        grid = [[1] * col for _ in range(row)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])

            return parent[i]

        def union(cells: List[tuple]) -> None:
            cell_1, cell_2 = cells
            i = cell_1[0]*col + cell_1[1]
            j = cell_2[0]*col + cell_2[1]
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j

        n = row*col
        ans = n
        for cell in reversed(cells):
            r, c = cell
            r -= 1
            c -= 1
            grid[r][c] = 0
            ans -= 1

            if r-1 >= 0 and grid[r-1][c] == 0: union([(r,c), (r-1, c)])
            if r+1 < row and grid[r+1][c] == 0: union([(r,c), (r+1, c)])
            if c+1 < col and grid[r][c+1] == 0: union([(r,c), (r, c+1)])
            if c-1 >= 0 and grid[r][c-1] == 0: union([(r,c), (r, c-1)])


            if r == 0: union([(r,c), (row-1, col)])
            if r == row-1: union([(r,c), (row-1, col+1)])

            if find(n) == find(n+1): break

        return ans