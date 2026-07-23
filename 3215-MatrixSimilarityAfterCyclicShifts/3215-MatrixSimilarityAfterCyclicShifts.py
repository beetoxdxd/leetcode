# Last updated: 22/7/2026, 11:35:33 p.m.
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n

        for i in range(len(mat)):
            if i % 2: aux = mat[i][k:] + mat[i][:k]
            else: aux = mat[i][n-k:] + mat[i][:n-k]

            if aux != mat[i]: return False

        return True