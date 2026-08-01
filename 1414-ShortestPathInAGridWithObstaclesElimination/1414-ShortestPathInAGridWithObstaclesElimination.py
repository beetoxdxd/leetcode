# Last updated: 1/8/2026, 5:24:25 p.m.
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3:
            return m + n - 2

        queue = deque([(0,0,k)])
        visited = {(0,0): k}
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        level = 0
        
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                x, y, obs = queue.popleft()

                if x == m-1 and y == n-1: return level

                for dx, dy in directions:
                    xp, yp = x + dx, y + dy

                    if xp < 0 or xp >= m or yp < 0 or yp >= n: continue
                    if grid[xp][yp] == 1 and obs == 0: continue

                    aux = obs-1 if grid[xp][yp] else obs
                        
                    if (xp, yp) in visited and aux <= visited[(xp, yp)]: continue
                            
                    queue.append((xp, yp, aux))
                    visited[(xp,yp)] = aux

            level += 1

        return -1