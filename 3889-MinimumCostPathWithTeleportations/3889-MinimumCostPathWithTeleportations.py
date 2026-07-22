# Last updated: 22/7/2026, 5:56:49 p.m.
import math

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[r][c] guarda el costo mínimo para estar en (r, c)
        dp = [[math.inf] * n for _ in range(m)]
        
        # El costo inicial es 0 (no pagas grid[0][0] porque no es un "destino")
        dp[0][0] = 0
        
        # --- CAPA 0: Movimientos normales (Derecha / Abajo) ---
        for r in range(m):
            for c in range(n):
                if r > 0: dp[r][c] = min(dp[r][c], dp[r-1][c] + grid[r][c])
                if c > 0: dp[r][c] = min(dp[r][c], dp[r][c-1] + grid[r][c])
        
        resultado_final = dp[m-1][n-1]
        
        # Agrupamos celdas por valor para procesar los saltos de forma masiva
        # y evitar el error de las celdas con el mismo valor.
        val_map = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in val_map: val_map[val] = []
                val_map[val].append((r, c))
        
        # Ordenamos los valores de mayor a menor
        sorted_values = sorted(val_map.keys(), reverse=True)

        # --- CAPAS 1 a K: Procesamos los saltos ---
        for _ in range(k):
            nueva_dp = [[math.inf] * n for _ in range(m)]
            mejor_costo_visto = math.inf
            
            # Procesamos por grupos de valor (Heurística MRV aplicada a valores)
            for v in sorted_values:
                # 1. Actualizamos el "mejor costo de origen" con todas las celdas de este valor
                for r, c in val_map[v]:
                    mejor_costo_visto = min(mejor_costo_visto, dp[r][c])
                
                # 2. Todas las celdas de este valor "heredan" el mejor costo visto (salto gratis)
                # También consideramos no saltar: min(mejor_visto, costo_anterior)
                for r, c in val_map[v]:
                    nueva_dp[r][c] = min(dp[r][c], mejor_costo_visto)
            
            # PASO B: Movimientos normales DESPUÉS del salto en esta capa
            for r in range(m):
                for c in range(n):
                    if r > 0: nueva_dp[r][c] = min(nueva_dp[r][c], nueva_dp[r-1][c] + grid[r][c])
                    if c > 0: nueva_dp[r][c] = min(nueva_dp[r][c], nueva_dp[r][c-1] + grid[r][c])
            
            dp = nueva_dp
            resultado_final = min(resultado_final, dp[m-1][n-1])
            if resultado_final == 0: break # Optimización: si ya es 0, no bajará más

        return resultado_final