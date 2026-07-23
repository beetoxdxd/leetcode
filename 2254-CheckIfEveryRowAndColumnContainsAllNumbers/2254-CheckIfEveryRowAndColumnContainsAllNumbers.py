# Last updated: 22/7/2026, 11:36:11 p.m.
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            count_row = set()
            count_col = set()

            for j in range(n):
                count_row.add(matrix[i][j])
                count_col.add(matrix[j][i])

            
            if len(count_row) != n or len(count_col) != n: return False

        return True
