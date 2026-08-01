# Last updated: 1/8/2026, 5:23:58 p.m.
class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6
        abc = 6
        limit = 10**9 + 7

        for i in range(1, n):
            new_aba = (3*aba + 2*abc) % limit
            new_abc = (2*aba + 2*abc) % limit

            aba, abc = new_aba, new_abc

        return (aba + abc) % limit