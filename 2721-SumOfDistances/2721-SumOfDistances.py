# Last updated: 22/7/2026, 11:35:49 p.m.
from collections import defaultdict

class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        # Agrupamos todos los índices donde aparece cada número
        grupos_indices = defaultdict(list)
        for i, num in enumerate(nums):
            grupos_indices[num].append(i)

        ans = [0] * len(nums)

        # Procesamos cada grupo de índices de forma independiente
        for indices in grupos_indices.values():
            n = len(indices)
            if n == 1:
                continue
            
            # Calculamos la suma total del grupo una sola vez
            total_sum = sum(indices)
            # Variable para llevar la suma de lo que vamos dejando a la izquierda
            left_sum = 0
            
            for i, val in enumerate(indices):
                # Cantidad de elementos a la derecha del actual
                count_right = n - 1 - i
                
                # La suma de la derecha se deduce por pura resta:
                # SumaDerecha = Total - SumaIzquierda - ValorActual
                right_sum = total_sum - left_sum - val
                
                # Aplicamos la lógica que dedujiste:
                # Distancia total = (i * val - left_sum) + (right_sum - count_right * val)
                ans[val] = (i * val - left_sum) + (right_sum - count_right * val)
                
                # Actualizamos la suma de la izquierda para la siguiente iteración
                left_sum += val
                
        return ans