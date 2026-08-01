# Last updated: 1/8/2026, 5:23:28 p.m.
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        size = 2**n - 1
        flip = False
        
        while size > 1:
            h = size >> 1
            if k == h+1:
                return '0' if flip else '1'

            if k > h+1: 
                flip = not flip
                k = size - k + 1

            size = h

        return '1' if flip else '0'