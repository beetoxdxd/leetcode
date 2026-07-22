# Last updated: 22/7/2026, 5:56:48 p.m.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True # Unión exitosa
        return False # Ya estaban conectados (formaría un ciclo)

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # 1. Separar aristas y validar las obligatorias (must == 1)
        must_edges = []
        optional_edges = []
        for e in edges:
            if e[3] == 1:
                must_edges.append(e)
            else:
                optional_edges.append(e)
        
        # Validación de Aristas Obligatorias:
        # No pueden formar ciclos y no pueden ser más de n-1
        dsu_must = DSU(n)
        for u, v, s, must in must_edges:
            if not dsu_must.union(u, v):
                return -1 # Ciclo detectado en aristas obligatorias
        
        if len(must_edges) >= n:
            return -1 # Demasiadas aristas para ser un árbol

        # 2. Búsqueda Binaria
        low = 0
        high = 2 * max((e[2] for e in edges), default=0)
        ans = -1

        def check(X):
            # Iniciamos DSU con las aristas obligatorias
            dsu = DSU(n)
            edges_count = 0
            
            for u, v, s, must in must_edges:
                if s < X: return False # Si una obligatoria es débil, X es imposible
                dsu.union(u, v)
                edges_count += 1
            
            # Aristas opcionales que NO necesitan mejora
            for u, v, s, must in optional_edges:
                if s >= X:
                    if dsu.union(u, v):
                        edges_count += 1
            
            # Aristas opcionales que SÍ necesitan mejora
            upgrades_used = 0
            for u, v, s, must in optional_edges:
                if s < X and 2 * s >= X:
                    if upgrades_used < k:
                        if dsu.union(u, v):
                            edges_count += 1
                            upgrades_used += 1
            
            # Es válido si conectamos todos los nodos (exactamente n-1 aristas)
            return dsu.components == 1 and edges_count == n - 1

        # 3. Ejecutar búsqueda
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans