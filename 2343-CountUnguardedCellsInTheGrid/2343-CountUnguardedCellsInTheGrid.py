# Last updated: 22/7/2026, 11:36:07 p.m.
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls + guards:
            grid[x][y] = 2

        cont = 0
        for guard in guards:
            # arriba
            i, j = guard[0]-1, guard[1]
            while i >= 0:
                if grid[i][j] == 2: break # es wall
                if grid[i][j] == 0:
                    cont += 1
                    grid[i][j] = 1 # indicamos que la celda ya se visitó
                i -= 1

            # derecha
            i, j = guard[0], guard[1]+1
            while j < n: 
                if grid[i][j] == 2: break # es wall
                if grid[i][j] == 0: 
                    cont += 1
                    grid[i][j] = 1
                j += 1

            # abajo
            i, j = guard[0]+1, guard[1]
            while i < m: 
                if grid[i][j] == 2: break # es wall
                if grid[i][j] == 0: 
                    cont += 1
                    grid[i][j] = 1
                i += 1

            # izquierda
            i, j = guard[0], guard[1]-1
            while j >= 0: 
                if grid[i][j] == 2: break # es wall
                if grid[i][j] == 0: 
                    cont += 1
                    grid[i][j] = 1
                j -= 1
            
        return m*n - cont - len(guards) - len(walls)
    