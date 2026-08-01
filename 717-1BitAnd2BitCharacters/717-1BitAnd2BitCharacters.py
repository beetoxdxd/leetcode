# Last updated: 1/8/2026, 5:26:15 p.m.
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        onebit = True

        while i < n:
            if bits[i] == 1: 
                i += 2
                onebit = False
            else: 
                i += 1
                onebit = True

        return onebit