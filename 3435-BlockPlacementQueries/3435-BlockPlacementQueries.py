# Last updated: 22/7/2026, 11:35:17 p.m.
from sortedcontainers import SortedList
from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        # Inicializamos el árbol con ceros
        self.tree = [0] * (4 * (n + 1))

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        
        # Guardamos siempre el espacio/hueco MÁXIMO
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        
        return max(p1, p2)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # 1. Encontramos el valor de 'x' más grande en todas las consultas
        # para darle al Segment Tree el tamaño exacto que necesita.
        max_x = max(q[1] for q in queries)
        
        tree = SegmentTree(max_x)
        sl = SortedList([0])  # Empezamos con un obstáculo imaginario en el origen (0)
        ans = []

        for query in queries:
            # --- QUERY TIPO 1: Añadir obstáculo ---
            if query[0] == 1:
                x = query[1]
                
                # Buscamos dónde cae 'x' entre los obstáculos actuales
                idx = sl.bisect_left(x)
                prev_obs = sl[idx - 1]  # Obstáculo a la izquierda
                
                # En la posición 'x' del árbol, guardamos el tamaño de su hueco izquierdo
                tree.update(1, 0, max_x, x, x - prev_obs)
                
                # Si había un obstáculo a la derecha, su hueco izquierdo se encogió
                if idx < len(sl):
                    nxt_obs = sl[idx]
                    tree.update(1, 0, max_x, nxt_obs, nxt_obs - x)
                
                # Finalmente, agregamos oficialmente el obstáculo a la lista ordenada
                sl.add(x)
                
            # --- QUERY TIPO 2: Verificar si cabe el bloque ---
            elif query[0] == 2:
                x = query[1]
                sz = query[2]
                
                # Encontramos el último obstáculo que está antes o exactamente en 'x'
                idx = sl.bisect_right(x) - 1
                prev_obs = sl[idx]
                
                # Paso A: Le preguntamos al árbol cuál es el hueco más grande
                # formado entre todos los obstáculos estrictamente dentro de [0, x]
                max_gap_in_tree = tree.query(1, 0, max_x, 0, x)
                
                # Paso B: Calculamos el pedazo "libre" final que va desde 
                # el último obstáculo detectado hasta el límite de la consulta 'x'
                partial_gap = x - prev_obs
                
                # El hueco real disponible es el mayor entre el Paso A y el Paso B
                total_max_gap = max(max_gap_in_tree, partial_gap)
                
                # Si el hueco máximo es mayor o igual al tamaño del bloque, cabe (True)
                ans.append(total_max_gap >= sz)
                
        return ans