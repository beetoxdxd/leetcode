# Last updated: 22/7/2026, 11:35:19 p.m.
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp0[i][j]: arreglos estables con i ceros y j unos que terminan en 0
        # dp1[i][j]: arreglos estables con i ceros y j unos que terminan en 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Casos base: arreglos que solo contienen un tipo de número
        # Solo son estables si no superan el límite
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Calcular dp0 (termina en 0)
                # Sumamos las dos opciones anteriores
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    # Restamos los casos que exceden el límite de ceros
                    # Estos casos son los que terminaban en 1 hace 'limit' pasos
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD
                
                # Calcular dp1 (termina en 1)
                dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j > limit:
                    # Restamos los casos que exceden el límite de unos
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD
                    
        return (dp0[zero][one] + dp1[zero][one]) % MOD