# Last updated: 22/7/2026, 5:56:07 p.m.
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        one_pair = False

        for i in range(1, 21):
            if n & (1 << i) and n & (1 << (i-1)): 
                if one_pair: return False
                one_pair = True

        return one_pair