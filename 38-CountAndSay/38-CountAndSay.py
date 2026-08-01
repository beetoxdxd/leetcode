# Last updated: 1/8/2026, 5:28:37 p.m.
class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"
        
        for i in range(1,n):
            cont = 1
            prev = rle[0]
            aux = ""

            for j in range(1,len(rle)):
                if rle[j] == prev: cont += 1
                else: 
                    aux += str(cont) + str(prev)
                    cont = 1
                    prev = rle[j]

            aux += str(cont) + str(prev)
            rle = aux

        return rle