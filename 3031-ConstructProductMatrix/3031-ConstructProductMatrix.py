# Last updated: 22/7/2026, 11:35:35 p.m.
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        p = [[0] * m for _ in range(n)]
        
        # Paso 1: Llenar la matriz con los SUFIJOS
        # Cada celda guardará el producto de todos los elementos después de ella
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD
        
        # Paso 2: Multiplicar por los PREFIJOS
        # Mantenemos un acumulador de lo que viene antes de la celda actual
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD
        
        return p