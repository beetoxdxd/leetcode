# Last updated: 1/8/2026, 5:24:02 p.m.
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],  # Street 1: Horizontal (left, right)
            2: [(1, 0), (-1, 0)],  # Street 2: Vertical (down, up)
            3: [(0, -1), (1, 0)],  # Street 3: Left-Down (left, down)
            4: [(0, 1), (1, 0)],   # Street 4: Right-Down (right, down)
            5: [(0, -1), (-1, 0)], # Street 5: Left-Up (left, up)
            6: [(0, 1), (-1, 0)]   # Street 6: Right-Up (right, up)
        }

        m = len(grid)
        n = len(grid[0])
        stack = [(0, 0)]
        visited = {(0, 0)}

        while stack:
            r, c = stack.pop()
            
            # ¿Llegamos al destino?
            if r == m - 1 and c == n - 1:
                return True
            
            # Probamos las salidas de la calle actual
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # 1. Dentro de límites y no visitado
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # 2. El "Apretón de Manos": 
                    # ¿La calle vecina tiene una salida que apunte de vuelta a nosotros?
                    # Si nosotros nos movimos (dr, dc), el vecino debe tener (-dr, -dc)
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
        
        return False