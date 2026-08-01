# Last updated: 1/8/2026, 5:23:00 p.m.
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = 0
        space = 1
        nxt = 2

        for i in range(1, n+1):
            if i == nxt:
                space += 1
                nxt <<= 1

            num = ((num << space) | i) % (10**9 + 7)

        return num