# Last updated: 1/8/2026, 5:24:20 p.m.
class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_pos(char_idx):
            # Retorna (fila, columna) para un índice de 0 a 25
            return (char_idx // 6, char_idx % 6)

        def dist(a, b):
            if a is None or b is None: return 0
            p1, p2 = get_pos(a), get_pos(b)
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # dp[p] representa el costo mínimo para llegar a la letra actual
        # teniendo el OTRO dedo en la posición 'p'. 
        # Usamos 26 para representar el estado "fuera del teclado" (None).
        dp = {26: 0} # {posicion_del_otro_dedo: costo_acumulado}

        for i in range(len(word)):
            new_dp = {}
            curr = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A') if i > 0 else None
            
            for other, cost in dp.items():
                # Opción 1: Mover el dedo que escribió la letra anterior (prev) a la actual (curr)
                # El "otro" dedo se queda donde estaba.
                d1 = dist(prev, curr)
                if other not in new_dp or cost + d1 < new_dp[other]:
                    new_dp[other] = cost + d1
                
                # Opción 2: Mover el "otro" dedo a la letra actual.
                # El dedo que estaba en 'prev' ahora se convierte en el "otro".
                # (Si i == 0, prev es None, lo cual es correcto)
                d2 = dist(other if other < 26 else None, curr)
                new_prev = prev if prev is not None else 26
                if new_prev not in new_dp or cost + d2 < new_dp[new_prev]:
                    new_dp[new_prev] = cost + d2
            
            dp = new_dp

        return min(dp.values())