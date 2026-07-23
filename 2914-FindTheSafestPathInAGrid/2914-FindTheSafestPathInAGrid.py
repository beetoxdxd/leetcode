# Last updated: 22/7/2026, 11:35:39 p.m.
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        queue = deque()
        distance = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: continue 
                queue.append((i, j, 0))
                visited[i][j] = True
                distance[i][j] = 0

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y, d = queue.popleft()

            for dx, dy in directions:
                xp, yp = x + dx, y + dy

                if xp < 0 or xp >= n or yp < 0 or yp >= n or visited[xp][yp]: continue
                distance[xp][yp] = d + 1
                visited[xp][yp] = True
                queue.append((xp, yp, d+1))

        visited = [[False] * n for _ in range(n)]
        heap = [(-distance[0][0], 0, 0)]
        heapq.heapify(heap)
        visited[0][0] = True

        while heap:
            sf, x, y = heapq.heappop(heap)
            sf *= -1

            if x == n-1 and y == n-1: return sf

            for dx, dy in directions:
                xp, yp = x + dx, y + dy
                if xp < 0 or xp >= n or yp < 0 or yp >= n or visited[xp][yp]: continue

                aux = min(sf, distance[xp][yp])
                visited[xp][yp] = True
                heapq.heappush(heap, (-aux, xp, yp))

        return 0