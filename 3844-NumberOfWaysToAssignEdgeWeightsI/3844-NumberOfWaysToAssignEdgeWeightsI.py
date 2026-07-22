# Last updated: 22/7/2026, 5:56:56 p.m.
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        # 1. Lista de listas en lugar de defaultdict (Sabiendo que N = len(edges) + 1)
        n = len(edges) + 1
        tree = [[] for _ in range(n + 1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # 2. Arreglo de booleanos en lugar de un set() para búsquedas ultra rápidas
        visited = [False] * (n + 1)
        visited[1] = True

        # 3. BFS por capas: guardamos solo los nodos, adiós a las tuplas
        current_layer = [1]
        max_depth = -1

        while current_layer:
            max_depth += 1
            next_layer = []
            
            # Procesamos toda la capa actual de un solo golpe
            for node in current_layer:
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        next_layer.append(neighbor)
            
            # Avanzamos a la siguiente generación
            current_layer = next_layer

        # Caso extremo: árbol de un solo nodo
        if max_depth == 0:
            return 0

        return pow(2, max_depth - 1, 10**9 + 7)