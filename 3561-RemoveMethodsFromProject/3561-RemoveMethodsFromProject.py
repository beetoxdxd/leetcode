# Last updated: 27/8/2026, 4:58:43 p.m.
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = [False] * n
        stack = [k]

        graph = defaultdict(list)
        for a,b in invocations:
            graph[a].append(b)

        visited[k] = True

        while stack:
            node = stack.pop()

            for element in graph[node]:
                if visited[element]: continue

                visited[element] = True
                stack.append(element)

        for a,b in invocations:
            if not visited[a] and visited[b]: return list(range(n))

        return [i for i in range(n) if not visited[i]]