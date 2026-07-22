# Last updated: 22/7/2026, 5:57:12 p.m.
import math

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = 0
        events = []
        for x, y, l in squares:
            area = l * l
            total_area += area
            events.append((y, 1, l))          # 1 para inicio
            events.append((y + l, -1, l))     # -1 para fin
        
        target_area = total_area / 2
        events.sort()
        
        accumulated_area = 0.0
        current_width_sum = 0
        prev_y = events[0][0]
        
        for i in range(len(events)):
            y, type_event, length = events[i]
            
            # Calculamos el área de la franja entre el Y anterior y el actual
            height = y - prev_y
            if height > 0:
                area_in_strip = height * current_width_sum
                
                if accumulated_area + area_in_strip >= target_area - 1e-12:
                    # Cálculo exacto por interpolación:
                    # Area_restante = (y_final - prev_y) * current_width_sum
                    needed_area = target_area - accumulated_area
                    return prev_y + (needed_area / current_width_sum)
                
                accumulated_area += area_in_strip
            
            # Actualizar el ancho total de los cuadrados que están "activos"
            if type_event == 1:
                current_width_sum += length
            else:
                current_width_sum -= length
            
            prev_y = y
            
        return float(prev_y)