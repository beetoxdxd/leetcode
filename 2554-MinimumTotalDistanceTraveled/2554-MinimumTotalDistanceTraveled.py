# Last updated: 22/7/2026, 11:35:59 p.m.
from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        # dp[j][i] = mínima distancia usando las primeras 'j' fábricas para 'i' robots
        # Inicializamos con un valor muy grande (infinito)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Caso base: 0 fábricas reparan 0 robots con costo 0
        dp[0][0] = 0
        
        for j, fact in enumerate(factory, 1): # Empezamos en 1 para usar j-1 fácilmente
            pos, limit = fact
            
            for i in range(n + 1):
                # Opción A: La fábrica actual no repara a ningún robot.
                # El costo es el mismo que el de la fábrica anterior para 'i' robots.
                dp[j][i] = dp[j-1][i]
                
                # Opción B: La fábrica actual repara 'l' robots (desde 1 hasta su límite).
                distance_accumulated = 0
                for l in range(1, limit + 1):
                    if i - l < 0: 
                        break # No hay suficientes robots hacia atrás
                    
                    # Sumamos la distancia del robot actual al acumulado del lote
                    distance_accumulated += abs(robot[i - l] - pos)
                    
                    # El costo total es: (distancia de este lote) + (mejor costo anterior)
                    if dp[j-1][i-l] != float('inf'):
                        cost = distance_accumulated + dp[j-1][i-l]
                        if cost < dp[j][i]:
                            dp[j][i] = cost
                            
        return dp[m][n]