# Last updated: 22/7/2026, 11:35:28 p.m.
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        target = k - 1  # Necesitamos k-1 elementos aparte del nums[0]
        
        # 1. Llenar ventana inicial
        # Tomamos los elementos desde el índice 1 hasta dist+1
        sl = SortedList(nums[1:dist + 2])
        
        # Calculamos la suma inicial de los 'target' más pequeños
        current_sum = sum(sl[:target])
        min_cost = nums[0] + current_sum
        
        # 2. Deslizar la ventana
        for i in range(dist + 2, n):
            in_v = nums[i]
            out_v = nums[i - dist - 1]
            
            # PASO A: Agregar el nuevo número
            sl.add(in_v)
            # Si el nuevo número entró en la zona "VIP" (los primeros target), actualizamos suma
            if sl.index(in_v) < target:
                current_sum += in_v - sl[target] # Sumamos el nuevo, restamos el que salió del top
            
            # PASO B: Quitar el número viejo
            idx_out = sl.index(out_v)
            if idx_out < target:
                # Si el que sale era parte de la suma, lo restamos y sumamos el suplente
                current_sum -= out_v
                current_sum += sl[target] # El mejor de la reserva entra al quite
            
            sl.remove(out_v)
            
            # Actualizar respuesta
            min_cost = min(min_cost, nums[0] + current_sum)
            
        return min_cost