# Last updated: 1/8/2026, 5:27:56 p.m.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        
        stack = [-1] # Inicializamos con -1 para facilitar el cálculo del ancho
        max_area = 0
        
        for i, h in enumerate(heights):
            # Mientras la barra actual sea más pequeña que la barra en el tope del stack,
            # significa que encontramos el límite derecho de la barra del stack.
            # Es hora de calcular el área de la barra del tope.
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            
            stack.append(i)
        
        return max_area