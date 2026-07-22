# Last updated: 22/7/2026, 5:57:13 p.m.
from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        h = defaultdict(list)
        
        # 1. Agrupamos índices: O(N)
        for i, num in enumerate(nums):
            h[num].append(i)
            
        # 2. Pre-calculamos la respuesta para CADA índice del arreglo: O(N)
        # Inicializamos con -1 por si el elemento es único
        min_distances = [-1] * n
        
        for num, indices in h.items():
            m = len(indices)
            if m > 1:
                for i in range(m):
                    curr = indices[i]
                    # Vecinos directos en la lista circular de índices
                    prev_i = indices[i - 1]          # Python maneja el -1 como el último
                    next_i = indices[(i + 1) % m]    # El siguiente con módulo
                    
                    # Distancia circular para el vecino izquierdo
                    d1 = abs(curr - prev_i)
                    d1 = min(d1, n - d1)
                    
                    # Distancia circular para el vecino derecho
                    d2 = abs(curr - next_i)
                    d2 = min(d2, n - d2)
                    
                    min_distances[curr] = min(d1, d2)
        
        # 3. Responder las consultas es ahora O(1) por cada una
        return [min_distances[q] for q in queries]