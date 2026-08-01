# Last updated: 1/8/2026, 5:27:24 p.m.
class Solution:
    def checkIsland(self, grid: List[List[str]], i: int, j: int) -> None:
        if grid[i][j] == "0": return

        grid[i][j] = "0"
        if i - 1 >= 0: self.checkIsland(grid, i-1, j) #arriba
        if j + 1 < len(grid[0]): self.checkIsland(grid, i, j+1) #derecha
        if i + 1 < len(grid): self.checkIsland(grid, i+1, j) #abajo
        if j - 1 >= 0: self.checkIsland(grid, i, j-1) #izquierda



    def numIslands(self, grid: List[List[str]]) -> int:
        cont = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.checkIsland(grid, i, j)
                    cont += 1
            
        return cont