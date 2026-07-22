# Last updated: 22/7/2026, 5:57:08 p.m.
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. Flat Arrays para la DLL
        vals = list(nums)
        prevs = [i - 1 for i in range(n)]
        nexts = [i + 1 for i in range(n)]
        nexts[n-1] = -1
        
        removed = [False] * n  # Array de booleanos es más rápido que un Set
        conflicts = 0
        pq = []

        # 2. Inicialización de conflictos y heap
        for i in range(n - 1):
            if vals[i] > vals[i+1]:
                conflicts += 1
            heapq.heappush(pq, (vals[i] + vals[i+1], i, i+1))

        ans = 0
        while conflicts > 0:
            s, L, R = heapq.heappop(pq)
            
            # Validaciones rápidas
            if removed[L] or removed[R] or nexts[L] != R:
                continue
            if s != vals[L] + vals[R]:
                continue

            # 3. Lógica de conflictos con Flat Arrays
            pL, nR = prevs[L], nexts[R]
            
            # Restar antiguos
            if pL != -1 and vals[pL] > vals[L]: conflicts -= 1
            if vals[L] > vals[R]: conflicts -= 1
            if nR != -1 and vals[R] > vals[nR]: conflicts -= 1

            # Fusionar
            removed[R] = True
            vals[L] = s
            nexts[L] = nR
            if nR != -1: prevs[nR] = L

            # Sumar nuevos
            if pL != -1 and vals[pL] > vals[L]: conflicts += 1
            if nR != -1 and vals[L] > vals[nR]: conflicts += 1

            # Nuevas sumas
            if pL != -1: heapq.heappush(pq, (vals[pL] + s, pL, L))
            if nR != -1: heapq.heappush(pq, (s + vals[nR], L, nR))

            ans += 1
            
        return ans