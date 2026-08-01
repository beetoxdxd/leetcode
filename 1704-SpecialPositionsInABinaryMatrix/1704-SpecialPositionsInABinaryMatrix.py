# Last updated: 1/8/2026, 5:23:25 p.m.
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        h = [sum(row) for row in mat]
        v = [sum(col) for col in zip(*mat)]

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and v[j] == 1 and h[i] == 1: ans += 1

        return ans