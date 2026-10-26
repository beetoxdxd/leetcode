# Last updated: 25/10/2026, 11:28:13 p.m.
1class Solution:
2    def countIslands(self, grid: List[List[int]], k: int) -> int:
3        directions = [(0,1),(1,0),(0,-1),(-1,0)]
4        m, n = len(grid), len(grid[0])
5        visited = [[False] * n for _ in range(m)]
6        queue = deque()
7        ans = 0
8
9        for i in range(m):
10            for j in range(n):
11                if visited[i][j] or grid[i][j] <= 0: continue
12
13                queue = deque([(i, j)])
14                visited[i][j] = True
15                val_island = 0
16
17                while queue:
18                    a, b = queue.popleft()
19                    val_island += grid[a][b]
20
21                    for dx, dy in directions:
22                        x, y = dx + a, dy + b
23
24                        if x < 0 or y < 0 or x >= m or y >= n: continue
25                        if visited[x][y] or grid[x][y] <= 0: continue
26
27                        visited[x][y] = True
28                        queue.append((x, y))
29
30                if val_island % k == 0: ans += 1
31
32        return ans