# Last updated: 22/7/2026, 5:56:57 p.m.
from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        tree = [[] for _ in range(n + 1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # ---- PREPROCESAMIENTO: BINARY LIFTING (LCA) ----
        LOG = 18  # 2^18 = 262,144 (suficiente para N = 10^5)
        depth = [0] * (n + 1)
        # up[j][i] guardará el ancestro número 2^j del nodo i
        up = [[0] * (n + 1) for _ in range(LOG)]

        # BFS para calcular las profundidades y el primer ancestro directo (2^0 = 1)
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            curr = queue.popleft()
            for neighbor in tree[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[curr] + 1
                    up[0][neighbor] = curr  # El padre directo
                    queue.append(neighbor)

        # Llenamos la tabla de ancestros usando programación dinámica
        for j in range(1, LOG):
            for i in range(1, n + 1):
                # Mi ancestro 2^j es el ancestro 2^(j-1) de mi ancestro 2^(j-1)
                up[j][i] = up[j - 1][up[j - 1][i]]

        # Función auxiliar para encontrar el LCA en O(log N)
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u  # Nos aseguramos de que 'u' sea el más profundo
            
            # Igualamos las profundidades subiendo 'u' espiritualmente
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[j][u]
            
            if u == v:
                return u

            # Subimos ambos nodos al mismo tiempo hasta encontrar el punto de separación
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            
            return up[0][u]

        # ---- RESPONDER LAS CONSULTAS EN O(log N) ----
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)  # Distancia 0, no hay aristas
                continue
                
            lca = get_lca(u, v)
            # Aplicamos la fórmula de la distancia en el árbol
            distance = depth[u] + depth[v] - 2 * depth[lca]
            
            # Aplicamos la misma matemática de paridad que descubriste en la versión I
            ans.append(pow(2, distance - 1, 10**9 + 7))

        return ans