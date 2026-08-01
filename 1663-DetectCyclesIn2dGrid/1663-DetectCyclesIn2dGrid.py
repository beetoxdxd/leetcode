# Last updated: 1/8/2026, 5:23:31 p.m.
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        for r in range(m):
            for c in range(n):
                # Si ya procesamos esta celda en un DFS anterior, la saltamos
                if (r, c) in visited:
                    continue
                
                # Iniciamos un DFS iterativo para esta "isla" de letras iguales
                char_objetivo = grid[r][c]
                # Stack guarda: (fila_actual, col_actual, fila_padre, col_padre)
                stack = [(r, c, -1, -1)]
                visited.add((r, c))
                
                while stack:
                    curr_r, curr_c, prev_r, prev_c = stack.pop()
                    
                    # Exploramos las 4 direcciones
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # 1. ¿Está dentro de la matriz?
                        if 0 <= nr < m and 0 <= nc < n:
                            # 2. ¿Es la misma letra que estamos rastreando?
                            if grid[nr][nc] == char_objetivo:
                                
                                # 3. ¿Es la celda de la que venimos justo ahora?
                                if (nr, nc) == (prev_r, prev_c):
                                    continue
                                
                                # 4. Si ya estaba en visited y NO es el padre... 
                                # ¡Felicidades, tienes un ciclo!
                                if (nr, nc) in visited:
                                    return True
                                
                                # 5. Si es nueva, la marcamos y seguimos explorando
                                visited.add((nr, nc))
                                stack.append((nr, nc, curr_r, curr_c))
                                
        return False