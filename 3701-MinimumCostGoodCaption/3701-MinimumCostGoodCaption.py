# Last updated: 22/7/2026, 5:57:14 p.m.
import math
from typing import List

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3: return ''
        
        abc = 'abcdefghijklmnopqrstuvwxyz'
        # Tu catálogo estático de diferencias de caracteres
        cost = [[abs(ord(c) - (97 + j)) for j in range(26)] for c in caption]
        
        # Pre-calculamos sumas acumuladas para obtener costos de rangos en O(1)
        pref = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for j in range(26):
                pref[i+1][j] = pref[i][j] + cost[i][j]
                
        def get_cost(l: int, r: int, letter_idx: int):
            return pref[r][letter_idx] - pref[l][letter_idx]

        # dp[i][j]: costo mínimo desde i si el bloque actual empieza con la letra j
        dp = [[math.inf] * 26 for _ in range(n + 1)]
        for j in range(26):
            dp[n][j] = 0

        # 1. Llenado de la matriz DP de atrás hacia adelante
        for i in range(n - 3, -1, -1):
            next_dp = dp[i+3]
            
            # Optimización para obtener el mínimo de la fila i+3 excluyendo la letra j en O(1)
            pref_min = [math.inf] * 27
            suff_min = [math.inf] * 27
            for j in range(26):
                pref_min[j+1] = min(pref_min[j], next_dp[j])
            for j in range(25, -1, -1):
                suff_min[j] = min(suff_min[j+1], next_dp[j])
                
            for j in range(26):
                # El menor costo del futuro excluyendo la letra j
                min_d = min(pref_min[j], suff_min[j+1])
                
                # Opción 1: Extender el bloque de la letra j por 1 carácter
                opt1 = cost[i][j] + dp[i+1][j] if i + 1 <= n else math.inf
                # Opción 2: Colocar exactamente 3 caracteres de j y obligar a cambiar de letra
                opt2 = get_cost(i, i+3, j) + min_d if i + 3 <= n else math.inf
                
                dp[i][j] = min(opt1, opt2)

        if min(dp[0]) == math.inf: return ''

        # 2. Reconstrucción de adelante hacia atrás
        ans = []
        i = 0
        current_char = -1
        
        while i < n:
            if current_char == -1:
                # Si estamos libres, elegimos la letra con el costo mínimo global
                target = min(dp[i])
                for j in range(26):
                    if dp[i][j] == target:
                        current_char = j
                        break
            
            j = current_char
            opt1 = cost[i][j] + dp[i+1][j] if i + 1 <= n else math.inf
            
            # Buscamos la mejor letra alternativa (k_best) para la Opción 2
            min_d = math.inf
            k_best = -1
            if i + 3 <= n:
                for k in range(26):
                    if k != j:
                        if dp[i+3][k] < min_d:
                            min_d = dp[i+3][k]
                            k_best = k
                            
            opt2 = get_cost(i, i+3, j) + min_d if i + 3 <= n else math.inf
            
            # Desempate alfabético perfecto
            choose_opt1 = False
            if opt1 < opt2:
                choose_opt1 = True
            elif opt2 < opt1:
                choose_opt1 = False
            else:
                # Si empatan en costo, comparamos los caracteres en la primera diferencia (posición i+3)
                # opt1 dejará la letra actual 'j', opt2 dejará la nueva letra 'k_best'
                choose_opt1 = (j < k_best)
                    
            if choose_opt1:
                ans.append(abc[j])
                i += 1
                # current_char sigue siendo j porque estamos extendiendo el bloque
            else:
                ans.append(abc[j] * 3)
                i += 3
                current_char = -1 # Cerramos bloque, el siguiente ciclo elegirá una nueva letra
                
        return "".join(ans)