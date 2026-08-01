# Last updated: 1/8/2026, 5:23:34 p.m.
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cont = numBottles
        full, empty = numBottles, 0
        
        while full > 0:
            total = full + empty
            full = total // numExchange
            empty = total % numExchange
            cont += full
        return cont