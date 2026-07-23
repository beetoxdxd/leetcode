# Last updated: 22/7/2026, 11:35:30 p.m.
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        # 1. Mapear cada cadena única a un ID numérico
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        num_nodes = len(unique_strs)
        
        # 2. Construir el grafo de conversiones (Matriz de Adyacencia)
        adj = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes): adj[i][i] = 0
        
        for o, c, z in zip(original, changed, cost):
            u, v = str_to_id[o], str_to_id[c]
            adj[u][v] = min(adj[u][v], z)
            
        # 3. Floyd-Warshall para encontrar costos mínimos entre todas las subcadenas
        # (Dado que num_nodes es manejable, FW funciona bien)
        for k in range(num_nodes):
            for i in range(num_nodes):
                if adj[i][k] == float('inf'): continue
                for j in range(num_nodes):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        
        # 4. DP para decidir cómo "partir" la cadena source
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Guardamos las longitudes de las subcadenas que podemos cambiar para no buscar de más
        lengths = sorted(list(set(len(s) for s in original)))
        
        for i in range(1, n + 1):
            # Opción A: Si el caracter actual es igual, el costo puede ser el del paso anterior
            if source[i-1] == target[i-1]:
                dp[i] = min(dp[i], dp[i-1])
            
            # Opción B: Intentar cambiar una subcadena que termine en i
            for l in lengths:
                if i - l < 0: break
                sub_s = source[i-l:i]
                sub_t = target[i-l:i]
                
                if sub_s in str_to_id and sub_t in str_to_id:
                    u, v = str_to_id[sub_s], str_to_id[sub_t]
                    costo_conversion = adj[u][v]
                    if costo_conversion != float('inf'):
                        dp[i] = min(dp[i], dp[i-l] + costo_conversion)
                        
        return dp[n] if dp[n] != float('inf') else -1