# Last updated: 22/7/2026, 11:35:45 p.m.
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)

        connected = [False] * n
        ans = 0

        for i in range(n):
            if connected[i]: continue

            queue = deque([i])
            visited = {i}
            edges = 0

            while queue:
                comp = queue.popleft()
                edges += len(graph[comp])

                for node in graph[comp]:
                    if node in visited: continue

                    visited.add(node)
                    queue.append(node)
                    connected[node] = True

            m = len(visited)
            if edges//2 == m*(m-1)//2: ans += 1

        return ans