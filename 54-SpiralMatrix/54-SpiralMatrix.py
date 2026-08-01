# Last updated: 1/8/2026, 5:28:18 p.m.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, l = len(matrix[0]), -1
        t, b = -1, len(matrix)
        i, j = 0, 0
        ans = []
        direction = 0

        while(l + 1 < r and t + 1 < b):
            ans.append(matrix[i][j])
            if direction == 0:
                j += 1
                if j != r: continue 
                t += 1
                i, j = t+1, r-1
                direction = 1
            elif direction == 1:
                i += 1
                if i != b: continue
                r -= 1
                j, i = r-1, b-1
                direction = 2
            elif direction == 2:
                j -= 1
                if j != l: continue
                b -= 1
                i, j = b-1, l+1
                direction = 3
            else:
                i -= 1
                if i != t: continue
                l += 1
                j, i = l+1, t+1
                direction = 0

        return ans