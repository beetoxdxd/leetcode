# Last updated: 27/8/2026, 4:58:06 p.m.
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            aux = n
            product = 1

            while aux:
                product *= aux % 10
                aux //= 10

            if product % t == 0: return n
            n += 1

        return 0