# Last updated: 22/7/2026, 5:57:06 p.m.
import math

class SegmentTree:
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords) - 1
        # count: cuántos cuadrados cubren este intervalo
        self.count = [0] * (4 * self.n)
        # length: longitud real cubierta en este intervalo
        self.length = [0.0] * (4 * self.n)

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.count[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2*v, tl, tm, l, min(r, tm), add)
            self.update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
        
        # Lógica clave: si este nodo está cubierto, su longitud es el ancho total
        if self.count[v] > 0:
            self.length[v] = self.coords[tr + 1] - self.coords[tl]
        else:
            # Si no está cubierto, hereda la longitud de sus hijos
            if tl != tr:
                self.length[v] = self.length[2*v] + self.length[2*v+1]
            else:
                self.length[v] = 0

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # 1. Compresión de Coordenadas X
        x_points = set()
        for x, y, l in squares:
            x_points.add(x)
            x_points.add(x + l)
        sorted_x = sorted(list(x_points))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        
        # 2. Eventos de Barrido en Y
        events = []
        for x, y, l in squares:
            # (y, tipo, x_inicio, x_fin)
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        st = SegmentTree(sorted_x)
        
        # 3. Primer Barrido: Calcular Área Total de la Unión
        total_area = 0.0
        strips = [] # Guardaremos las franjas para el segundo paso
        
        for i in range(len(events) - 1):
            y, type, x1, x2 = events[i]
            # Actualizamos el Segment Tree con el intervalo comprimido
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            
            # El ancho actual es la raíz del Segment Tree
            current_width = st.length[1]
            dy = events[i+1][0] - y
            if dy > 0:
                area_strip = current_width * dy
                total_area += area_strip
                strips.append((y, events[i+1][0], current_width))

        # 4. Segundo Barrido: Encontrar el punto de corte
        target_area = total_area / 2
        accumulated_area = 0.0
        
        for y_start, y_end, width in strips:
            if width == 0: continue
            
            area_strip = width * (y_end - y_start)
            if accumulated_area + area_strip >= target_area - 1e-12:
                # Interpolación final
                needed = target_area - accumulated_area
                return y_start + (needed / width)
            
            accumulated_area += area_strip
            
        return float(events[-1][0])