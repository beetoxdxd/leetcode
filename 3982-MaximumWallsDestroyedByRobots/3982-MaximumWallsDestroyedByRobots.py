# Last updated: 22/7/2026, 5:56:33 p.m.
import bisect

class Solution:
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        # 1. Limpiar y ordenar datos
        walls = sorted(list(set(walls)))
        rb = sorted(zip(robots, distance))
        robots_pos = [x[0] for x in rb]
        dists = [x[1] for x in rb]
        n = len(robots_pos)
        
        # 2. Identificar muros en posiciones de robots
        rob_set = set(robots_pos)
        walls_at_robots = 0
        is_robot_pos = [False] * len(walls)
        for i, w in enumerate(walls):
            if w in rob_set:
                is_robot_pos[i] = True
                walls_at_robots += 1
        
        # Pre-calcular sumas de prefijos para contar muros que NO están en robots
        pref_rob = [0] * (len(walls) + 1)
        for i in range(len(walls)):
            pref_rob[i+1] = pref_rob[i] + (1 if is_robot_pos[i] else 0)

        def count_no_rob(low, high):
            if low > high: return 0
            idx1 = bisect.bisect_left(walls, low)
            idx2 = bisect.bisect_right(walls, high)
            total_in_range = idx2 - idx1
            robs_in_range = pref_rob[idx2] - pref_rob[idx1]
            return total_in_range - robs_in_range

        # 3. DP: dp[i][0] fired LEFT, dp[i][1] fired RIGHT
        dp = [[0, 0] for _ in range(n)]
        
        # Caso inicial: Primer robot
        # Si dispara a la izquierda, limpia su zona inicial
        dp[0][0] = count_no_rob(robots_pos[0] - dists[0], robots_pos[0] - 1)
        dp[0][1] = 0 # No limpia nada a su izquierda si dispara a la derecha
        
        for i in range(1, n):
            r_prev, r_curr = robots_pos[i-1], robots_pos[i]
            d_prev, d_curr = dists[i-1], dists[i]
            
            # Muros en el intervalo (r_prev, r_curr)
            # S1: i-1 dispara a la derecha
            s1_limit = min(r_prev + d_prev, r_curr - 1)
            c_s1 = count_no_rob(r_prev + 1, s1_limit)
            
            # S2: i dispara a la izquierda
            s2_limit = max(r_curr - d_curr, r_prev + 1)
            c_s2 = count_no_rob(s2_limit, r_curr - 1)
            
            # Union: Si los disparos se cruzan o tocan, cubren TODO el intervalo
            if s1_limit >= s2_limit:
                c_union = count_no_rob(r_prev + 1, r_curr - 1)
            else:
                c_union = c_s1 + c_s2
            
            # Robot i dispara a la IZQUIERDA:
            # - Si i-1 disparó a la izquierda, i limpia su parte de S2
            # - Si i-1 disparó a la derecha, se cuenta la unión de ambos
            dp[i][0] = max(dp[i-1][0] + c_s2, dp[i-1][1] + c_union)
            
            # Robot i dispara a la DERECHA:
            # - Si i-1 disparó a la izquierda, el intervalo queda vacío (i no dispara hacia él)
            # - Si i-1 disparó a la derecha, i-1 limpia su parte de S1
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + c_s1)
            
        # 4. Resultado final
        # El último robot puede limpiar muros a su derecha si disparó a la derecha
        muros_finales = count_no_rob(robots_pos[-1] + 1, robots_pos[-1] + dists[-1])
        
        return max(dp[-1][0], dp[-1][1] + muros_finales) + walls_at_robots