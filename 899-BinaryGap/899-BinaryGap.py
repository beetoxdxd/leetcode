# Last updated: 1/8/2026, 5:25:38 p.m.
class Solution:
    def binaryGap(self, n: int) -> int:
        cont = 0
        while n & 1 == 0: 
            n = n >> 1
            cont += 1

        ans = 0 
        dif = 1
        for i in range(cont, 32):
            n = n >> 1
            if n & 1: 
                ans = max(ans, dif)
                dif = 1
            else: dif += 1

        return ans