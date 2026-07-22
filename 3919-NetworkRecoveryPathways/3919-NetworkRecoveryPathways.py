# Last updated: 22/7/2026, 5:56:47 p.m.
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = defaultdict(list)
        n = len(online)
        l = math.inf
        r = 0

        for u, v, cost in edges:
            if online[u] and online[v]: 
                graph[u].append((v, cost))
                l = min(l, cost)
                r = max(r, cost)

        
        ans = -1

        while l <= r:
            mid = (l+r) // 2
            heap = [(0, 0)]
            heapq.heapify(heap)
            visited = [math.inf] * n
            visited[0] = 0

            while heap:
                acc, u = heapq.heappop(heap)
                if acc > visited[u]: continue

                if u == n-1:
                    break

                for v, cost in graph[u]:
                    aux = acc + cost

                    if cost < mid or aux > k or visited[v] <= aux: continue
                    heapq.heappush(heap, (aux, v))
                    visited[v] = aux

            if visited[n-1] <= k:
                ans = mid
                l = mid + 1
            else: r = mid - 1

        return ans