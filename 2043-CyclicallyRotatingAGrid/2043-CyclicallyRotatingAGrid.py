# Last updated: 1/8/2026, 5:22:21 p.m.
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def traverse(left, right, down, up):
            elements = []

            # start, end, inc, z, flag
            mov = [
                (left, right+1, 1, up, 0),
                (up+1, down+1, 1, right, 1),
                (right-1, left, -1, down, 0),
                (down, up, -1, left, 1)
            ]

            for start, end, inc, z, flag in mov:
                for i in range(start, end, inc):
                    elements.append(grid[i][z]) if flag else elements.append(grid[z][i])

            n = len(elements)
            x = k % n #(2*(right+1-left) + 2*(down+1-up) - 4)

            for start, end, inc, z, flag in mov:
                for i in range(start, end, inc):
                    if flag: ans[i][z] = elements[x]
                    else: ans[z][i] = elements[x]

                    x = (x+1) % n
            
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for i in range(min(m, n)//2):
            traverse(i, n-1-i, m-1-i, i)

        return ans