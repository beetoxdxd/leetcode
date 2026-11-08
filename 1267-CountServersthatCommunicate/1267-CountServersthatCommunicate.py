# Last updated: 8/11/2026, 1:22:04 a.m.
1class Solution:
2    def countServers(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        rows, cols = [0] * m, [0] * n
5        servers = 0
6        
7        for i in range(m):
8            for j in range(n):
9                if grid[i][j] == 0: 
10                    continue
11
12                rows[i] += 1
13                cols[j] += 1
14                servers += 1
15
16        for i in range(m):
17            for j in range(n):
18                if grid[i][j] == 0: 
19                    continue
20                    
21                if rows[i] == 1 and cols[j] == 1: servers -= 1
22
23        return servers