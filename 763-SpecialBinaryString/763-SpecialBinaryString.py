# Last updated: 1/8/2026, 5:25:57 p.m.
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            # Llevamos el conteo de 1s y 0s
            count += 1 if char == '1' else -1
            
            # Cuando el contador llega a 0, encontramos un "Special Binary String" independiente
            if count == 0:
                # Recursivamente procesamos el interior: s[i+1 : j]
                # Quitamos el primer '1' y el último '0' para resolver lo de adentro
                inner = self.makeLargestSpecial(s[i + 1 : j])
                res.append('1' + inner + '0')
                i = j + 1
        
        # Ordenamos los bloques encontrados de mayor a menor para maximizar el valor
        res.sort(reverse=True)
        
        return "".join(res)