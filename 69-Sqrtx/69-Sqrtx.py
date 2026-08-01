# Last updated: 1/8/2026, 5:28:00 p.m.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        i, j = 1, x
        while i <= j:
            h = (i+j) // 2
            mult = h*h

            if mult == x: return h
            if mult > x: j = h-1
            else: i = h+1

        return j