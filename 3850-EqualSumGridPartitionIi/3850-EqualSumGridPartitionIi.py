# Last updated: 22/7/2026, 5:56:54 p.m.
from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def solve(g):
            m = len(g)
            n = len(g[0])
            row_sums = [sum(r) for r in g]
            total = sum(row_sums)
            
            # Inicialización rápida del diccionario de frecuencias
            bot_freq = defaultdict(int)
            for r in range(m):
                for val in g[r]:
                    bot_freq[val] += 1
            
            top_freq = defaultdict(int)
            acum, target = 0, total
            
            for i in range(m - 1):
                # Movemos la fila completa del bloque inferior al superior
                current_row = g[i]
                for val in current_row:
                    top_freq[val] += 1
                    bot_freq[val] -= 1
                    if bot_freq[val] == 0:
                        del bot_freq[val]
                
                row_sum = row_sums[i]
                acum += row_sum
                target -= row_sum
                
                if acum == target: return True
                
                # Caso 1: Descontar de la sección SUPERIOR (filas 0 a i)
                diff = acum - target
                if diff > 0:
                    # Es 2D si tiene >1 fila Y >1 columna. Si es 1D, solo extremos.
                    if (i > 0 and n > 1):
                        if diff in top_freq: return True
                    else:
                        # Sección 1D: solo podemos quitar las puntas
                        if g[0][0] == diff or g[i][n-1] == diff: return True
                
                # Caso 2: Descontar de la sección INFERIOR (filas i+1 a m-1)
                diff = target - acum
                if diff > 0:
                    # Es 2D si quedan >1 fila Y hay >1 columna
                    if (i < m - 2 and n > 1):
                        if diff in bot_freq: return True
                    else:
                        # Sección 1D: solo puntas del bloque restante
                        if g[i+1][0] == diff or g[m-1][n-1] == diff: return True
            
            return False

        # Ejecutamos para cortes horizontales
        if solve(grid): return True
        # Transponemos para que los cortes verticales sean horizontales y reutilizar solve
        transposed = list(zip(*grid))
        return solve(transposed)