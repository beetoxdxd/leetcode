# Last updated: 1/8/2026, 5:23:33 p.m.
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 1. Contamos cuántos ceros tiene cada fila al final
        trailing_zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        ans = 0
        # 2. Estrategia Greedy: Para cada posición i, buscamos la fila adecuada
        for i in range(n):
            target = n - 1 - i  # Ceros mínimos necesarios para la fila i
            
            # Buscamos la primera fila desde i hacia abajo que cumpla
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
            
            # Si no encontramos ninguna, es imposible
            if found_idx == -1:
                return -1
            
            # 3. Simulamos los swaps y sumamos el costo
            # Movemos la fila encontrada hasta la posición i
            ans += (found_idx - i)
            
            # Reorganizamos la lista (sacamos de found_idx e insertamos en i)
            row_to_move = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, row_to_move)
            
        return ans