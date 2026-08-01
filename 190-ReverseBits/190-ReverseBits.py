# Last updated: 1/8/2026, 5:27:26 p.m.
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if n & (1 << i): ans = ans | (1 << (31-i))

        return ans