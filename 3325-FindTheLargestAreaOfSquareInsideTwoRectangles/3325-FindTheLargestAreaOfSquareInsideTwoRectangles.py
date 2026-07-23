# Last updated: 22/7/2026, 11:35:26 p.m.
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Comparamos cada par (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # Coordenadas del Rectángulo i
                ax1, ay1 = bottomLeft[i]
                cx1, cy1 = topRight[i]
                
                # Coordenadas del Rectángulo j
                ax2, ay2 = bottomLeft[j]
                cx2, cy2 = topRight[j]
                
                # Calcular intersección
                # El inicio de la intersección es el máximo de los inicios
                inter_ax = max(ax1, ax2)
                inter_ay = max(ay1, ay2)
                
                # El fin de la intersección es el mínimo de los fines
                inter_cx = min(cx1, cx2)
                inter_cy = min(cy1, cy2)
                
                # Calcular ancho y alto
                width = inter_cx - inter_ax
                height = inter_cy - inter_ay
                
                # Si hay intersección válida (ancho y alto positivos)
                if width > 0 and height > 0:
                    # El lado del cuadrado está limitado por la dimensión más pequeña
                    side = min(width, height)
                    max_side = max(max_side, side)
                    
        return max_side * max_side
