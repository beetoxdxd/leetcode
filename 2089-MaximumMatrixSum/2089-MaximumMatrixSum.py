# Last updated: 1/8/2026, 5:22:16 p.m.
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negs = 0
        ans = 0
        min_value = math.inf

        for row in matrix:
            for col in row:
                if col <= 0: negs += 1
                col_abs = abs(col)
                min_value = min(min_value, col_abs)
                ans += col_abs

        if negs % 2 == 0: return ans
        return ans - 2*min_value