# Last updated: 22/7/2026, 11:35:09 p.m.
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1: health -= 1
        visited = [[False] * n for _ in range(m)]
        heap = [(-health, 0, 0)]
        heapq.heapify(heap)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while heap:
            h, x, y = heapq.heappop(heap)
            h *= -1

            if x == m-1 and y == n-1 and h >= 1: return True

            for dx, dy in directions:
                xp, yp = x + dx, y + dy

                if xp < 0 or xp >= m or yp < 0 or yp >= n or visited[xp][yp]: continue
                if grid[xp][yp] == 1: aux = h-1
                else: aux = h

                visited[xp][yp] = True
                if aux < 1: continue

                heapq.heappush(heap, (-aux, xp, yp))

        return False