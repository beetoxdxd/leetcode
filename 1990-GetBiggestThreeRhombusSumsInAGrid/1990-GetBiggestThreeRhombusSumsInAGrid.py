# Last updated: 1/8/2026, 5:22:29 p.m.
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        for i in range(m):
            for j in range(n):
                limit = 1
                
                if grid[i][j] not in ans:
                    aux = min(ans) if ans else 0
                    if len(ans) < 3: ans.append(grid[i][j])
                    elif grid[i][j] > aux:
                        ans.remove(min(ans))
                        ans.append(grid[i][j])

                while j + limit < n and j - limit >= 0 and i + limit*2 < m:
                    acc = grid[i][j] + grid[i+limit][j+limit] + grid[i+limit][j-limit] + grid[i+limit*2][j]
                    for k in range(1, limit):
                        acc += grid[i+k][j+k] + grid[i+limit*2-k][j+k] + grid[i+k][j-k] + grid[i+limit*2-k][j-k]

                    limit += 1

                    if acc not in ans:
                        aux = min(ans)
                        if acc > aux:
                            if len(ans) == 3: ans.remove(aux)
                            ans.append(acc)

        return sorted(ans, reverse=True)