# Last updated: 22/7/2026, 5:56:32 p.m.
from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        initial_zeros = s.count('0')
        if initial_zeros == 0:
            return 0
        
        # parent[i] nos servirá para saltar estados ya visitados
        # Necesitamos manejar paridad par e impar por separado
        parent = list(range(n + 3))
        
        def find(i):
            # Versión iterativa de find para evitar RecursionError
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                new_i = parent[i]
                parent[i] = root
                i = new_i
            return root

        queue = deque([(initial_zeros, 0)])
        
        # Marcamos el estado inicial como visitado apuntando al siguiente de su misma paridad
        parent[initial_zeros] = initial_zeros + 2
        
        while queue:
            u, steps = queue.popleft()
            
            # El rango de ceros alcanzables [L, R] tiene una lógica matemática:
            # El mínimo de ceros (L) ocurre cuando priorizamos convertir 0s en 1s.
            # El máximo de ceros (R) ocurre cuando priorizamos convertir 1s en 0s.
            L = abs(u - k)
            R = n - abs(n - u - k)
            
            # La paridad del nuevo número de ceros siempre es (u + k) % 2
            curr = find(L) if L % 2 == (u + k) % 2 else find(L + 1)
            
            while curr <= R:
                if curr == 0:
                    return steps + 1
                
                queue.append((curr, steps + 1))
                
                # "Borramos" el estado actual de los disponibles
                # conectándolo con el siguiente de su misma paridad
                parent[curr] = find(curr + 2)
                curr = parent[curr]
                
        return -1