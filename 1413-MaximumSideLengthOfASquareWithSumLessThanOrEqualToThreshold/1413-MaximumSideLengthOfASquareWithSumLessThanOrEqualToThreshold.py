# Last updated: 1/8/2026, 5:24:27 p.m.
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] + mat[i][j] - prefix[i][j]

        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                k = ans + 1

                if i >= k and j >= k:
                    s = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
                    if s <= threshold: ans = k
                    
                    
        return ans