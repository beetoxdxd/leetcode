# Last updated: 1/8/2026, 5:22:49 p.m.
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [0]*n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]: heights[j] += 1
                else: heights[j] = 0

            heights_s = sorted(heights)

            for j in range(n):
                ans = max(ans, heights_s[j] * (n-j))

        return ans