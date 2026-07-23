# Last updated: 22/7/2026, 11:35:51 p.m.
class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        ans = [0] * n
        curr_char = 1 # Representa 'a', 2 es 'b', etc.
        
        # 1. Construcción Greedy
        for i in range(n):
            if ans[i] > 0: continue
            if curr_char > 26: return "" # Nos quedamos sin letras
            
            for j in range(i, n):
                if lcp[i][j] > 0:
                    ans[j] = curr_char
            curr_char += 1
            
        # Convertir números a letras (1 -> 'a', 2 -> 'b')
        word = "".join(chr(ord('a') + v - 1) for v in ans)
        
        # 2. Verificación con Programación Dinámica
        # Creamos una matriz LCP desde nuestra 'word' para comparar
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = 0
                
                # Si no coincide con la original, la palabra es inválida
                if dp[i][j] != lcp[i][j]:
                    return ""
                    
        return word