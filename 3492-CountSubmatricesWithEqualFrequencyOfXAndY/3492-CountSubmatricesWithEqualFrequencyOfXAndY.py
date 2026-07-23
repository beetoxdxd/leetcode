# Last updated: 22/7/2026, 11:35:14 p.m.
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        upper_row = [0] * (n+1)
        boolean = [False] * n
        ans = 0

        for i in range(m):
            prev_boolean = False
            diag = 0

            for j in range(n):
                if grid[i][j] == 'X': elem = 1; boolean[j] = True
                elif grid[i][j] == 'Y': elem = -1
                else: elem = 0

                aux = upper_row[j+1]
                upper_row[j+1] = upper_row[j+1] + upper_row[j] - diag + elem
                diag = aux

                if prev_boolean or boolean[j]: boolean[j] = True
                prev_boolean = boolean[j]

                if upper_row[j+1] == 0 and boolean[j]: ans += 1

        return ans