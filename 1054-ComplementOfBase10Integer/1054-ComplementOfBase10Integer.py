# Last updated: 1/8/2026, 5:25:13 p.m.
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1

        pos = 0
        ans = 0
        
        while n > 0:
            if n & 1 == 0:
                ans = ans | (1 << pos)

            n >>= 1
            pos += 1

        return ans