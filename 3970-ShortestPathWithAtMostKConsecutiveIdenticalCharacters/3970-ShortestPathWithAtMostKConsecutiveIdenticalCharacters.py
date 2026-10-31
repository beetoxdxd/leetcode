# Last updated: 31/10/2026, 1:25:01 p.m.
1class Solution:
2    def shortestPath(
3        self, n: int, edges: List[List[int]], labels: str, k: int
4    ) -> int:
5        g = [[] for _ in range(n)]
6        for x, y, w in edges:
7            g[x].append((y, w))
8
9        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
10        # {shortest path length, node index, number of consecutive identical letters at the end}
11        pq = []
12
13        dis[0][1] = 0
14        heappush(pq, (0, 0, 1))
15
16        while pq:
17            d, x, cnt = heappop(pq)
18
19            if d > dis[x][cnt]:
20                continue
21            if x == n - 1:
22                return d
23
24            for y, w in g[x]:
25                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
26                if new_cnt > k:
27                    continue
28
29                nd = d + w
30                if nd < dis[y][new_cnt]:
31                    dis[y][new_cnt] = nd
32                    heappush(pq, (nd, y, new_cnt))
33
34        return -1