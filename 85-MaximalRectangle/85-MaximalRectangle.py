# Last updated: 1/8/2026, 5:27:53 p.m.
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0])+1)
        max_area = 0

        for row in matrix:
            for i in range(len(row)):
                if row[i] == '1': heights[i] += 1
                else: heights[i] = 0

            stack = [-1]

            for i, h in enumerate(heights):
                while stack[-1] != -1 and h < heights[stack[-1]]:
                    current_h = heights[stack.pop()]
                    current_w = i - stack[-1] - 1
                    max_area = max(max_area, current_h * current_w)

                stack.append(i)

        return max_area