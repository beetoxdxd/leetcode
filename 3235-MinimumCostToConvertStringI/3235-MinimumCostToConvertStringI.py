# Last updated: 22/7/2026, 11:35:31 p.m.
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[math.inf] * 26 for _ in range(26)]
        for i in range(26): graph[i][i] = 0

        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')

            if cost[i] < graph[u][v]: graph[u][v] = cost[i]

        min_costs = []
        for i in range(26):
            distancias = [math.inf] * 26
            distancias[i] = 0
            pq = []
            heapq.heappush(pq, (0, i))

            while pq:
                curr_cost, u = heapq.heappop(pq)
                if curr_cost > distancias[u]: continue

                for v in range(26):
                    if graph[u][v] != math.inf and graph[u][v] + curr_cost < distancias[v]: 
                        distancias[v] = graph[u][v] + curr_cost
                        heapq.heappush(pq, (graph[u][v] + curr_cost, v))

            min_costs.append(distancias[:])

        ans = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                value = min_costs[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
                if value != math.inf: ans += value
                else: return -1

        return ans
            