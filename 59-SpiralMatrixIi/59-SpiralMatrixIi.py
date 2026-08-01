# Last updated: 1/8/2026, 5:28:09 p.m.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)
        l, t, r, b = -1, -1, n, n
        i, j = 0, 0
        direction = 0

        for cont in range(1, n*n + 1):
            matrix[i][j] = cont
            cont += 1
            
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

        return matrix