# Last updated: 1/8/2026, 5:22:23 p.m.
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
            equal = True

            for i in range(n):
                for j in range(n):
                    if i < j: mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                
                mat[i] = list(reversed(mat[i]))
                if mat[i] != target[i]: equal = False

            if equal: return True

        return False