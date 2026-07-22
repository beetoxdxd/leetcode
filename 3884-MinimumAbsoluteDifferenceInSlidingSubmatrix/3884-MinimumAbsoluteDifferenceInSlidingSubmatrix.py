# Last updated: 22/7/2026, 5:56:51 p.m.
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                distinct = set()

                for x in range(i, k+i):
                    for y in range(j, k+j):
                        distinct.add(grid[x][y])

                distinct = sorted(distinct)
                diff = math.inf
                for x in range(len(distinct)-1):
                    diff = min(diff, abs(distinct[x]-distinct[x+1]))

                ans[i][j] = diff if diff != math.inf else 0

        return ans