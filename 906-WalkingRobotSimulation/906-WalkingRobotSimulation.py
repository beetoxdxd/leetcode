# Last updated: 1/8/2026, 5:25:34 p.m.
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Definimos vectores: 0:N, 1:E, 2:S, 3:W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        curr_dir = 0
        max_dist_sq = 0
        
        # O(M) para crear el set
        obstacle_set = {tuple(o) for o in obstacles}

        for cmd in commands:
            if cmd == -2:   # Izquierda
                curr_dir = (curr_dir - 1) % 4
            elif cmd == -1: # Derecha
                curr_dir = (curr_dir + 1) % 4
            else:
                dx, dy = dirs[curr_dir]
                for _ in range(cmd):
                    # Predecimos la siguiente posición
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    # Actualizamos el máximo en cada paso
                    max_dist_sq = max(max_dist_sq, x*x + y*y)
        
        return max_dist_sq