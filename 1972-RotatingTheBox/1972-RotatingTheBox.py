# Last updated: 1/8/2026, 5:22:35 p.m.
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        ans = [['.'] * n for _ in range(m)] 

        for i in range(m):
            stones = []
            cont = 0
            for el in boxGrid[i]:
                if el == '*': stones.append(cont); cont = 0
                elif el == '#': cont +=1
            
            k = n-1
            curr = cont

            while k >= 0:
                if boxGrid[i][k] == '*': 
                    ans[i][k] = '*'
                    curr = stones.pop()
                elif curr > 0:
                    ans[i][k] = '#'
                    curr -= 1

                k -= 1

        return [list(row[::-1]) for row in zip(*ans)]