# Last updated: 22/7/2026, 5:56:50 p.m.
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        naturals = [[] for _ in range(n)]
        reversals = [[] for _ in range(n)]
        dist = [math.inf] * n

        for edge in edges:
            u, v, w = edge
            naturals[u].append((v, w))
            reversals[v].append((u, 2*w))

        pq = []
        heapq.heappush(pq, (0,0))
        dist[0] = 0

        while pq:
            curr_cost, u = heapq.heappop(pq)
            if u == n-1: return curr_cost
            if curr_cost > dist[u]: continue

            for v,w in naturals[u]:
                cost = curr_cost + w
                if cost < dist[v]:
                    dist[v] = cost
                    heapq.heappush(pq, (cost, v))

            for v,w in reversals[u]:
                cost = curr_cost + w
                if cost < dist[v]:
                    dist[v] = cost
                    heapq.heappush(pq, (cost, v))

        return -1

