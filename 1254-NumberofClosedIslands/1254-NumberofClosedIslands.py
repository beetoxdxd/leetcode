# Last updated: 26/10/2026, 12:05:46 a.m.
1class Solution:
2    def closedIsland(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        visited = [[False] * n for _ in range(m)]
5        directions = [(1,0), (0,1), (-1,0), (0,-1)]
6        islands = 0
7
8        for i in range(m):
9            for j in range(n):
10                if grid[i][j] == 1 or visited[i][j]: continue
11
12                queue = deque([(i, j)])
13                visited[i][j] = True
14                closed = True
15
16                while queue:
17                    a, b = queue.popleft()
18                    if a == 0 or a == m-1 or b == 0 or b == n-1: closed = False
19                    
20                    for dx, dy in directions:
21                        x, y = dx + a, b + dy
22
23                        if x < 0 or y < 0 or x >= m or y >= n: continue
24                        if visited[x][y] or grid[x][y] == 1: continue
25
26                        queue.append((x, y))
27                        visited[x][y] = True
28
29                if closed: islands += 1
30
31        return islands