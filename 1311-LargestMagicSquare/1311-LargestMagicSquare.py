# Last updated: 1/8/2026, 5:24:38 p.m.
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pref_row = [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pref_row[i][j+1] += pref_row[i][j] + grid[i][j]

        pref_col = [[0]*n for _ in range(m+1)]
        for j in range(n):
            for i in range(m):
                pref_col[i+1][j] += pref_col[i][j] + grid[i][j]

        pref_diag1 = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                pref_diag1[i+1][j+1] = pref_diag1[i][j] + grid[i][j]

        pref_diag2 = [[0]*(n+2) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                pref_diag2[i+1][j+1] = pref_diag2[i][j+2] + grid[i][j]
        
        def traverse(l: int, r: int, c: int) -> bool:
            target = pref_row[r][c+l] - pref_row[r][c]
            
            for i in range(r + 1, r + l):
                if pref_row[i][c + l] - pref_row[i][c] != target:
                    return False
            
            for j in range(c, c + l):
                if pref_col[r+l][j] - pref_col[r][j] != target:
                    return False
            
            d1 = pref_diag1[r + l][c + l] - pref_diag1[r][c]
            d2 = pref_diag2[r + l][c + 1] - pref_diag2[r][c + l + 1]
            
            return d1 == target and d2 == target
        
        ans = 1
        for i in range(m):
            for j in range(n):
                l = ans
                while i + l < m and j + l < n:
                    if traverse(l+1, i, j): 
                        ans = l+1
                    l += 1

        return ans