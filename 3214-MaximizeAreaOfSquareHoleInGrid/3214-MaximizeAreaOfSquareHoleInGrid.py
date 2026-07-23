# Last updated: 22/7/2026, 11:35:34 p.m.
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest(bars: List[int]) -> int:
            bars.sort()
            x, y = bars[0], bars[0]
            ansx, ansy = x, y

            for i in range(1, len(bars)):
                if bars[i] != bars[i-1]+1:
                    x = bars[i]
                y = bars[i]

                if y - x >= ansy - ansx:
                    ansx, ansy = x, y

            return ansy-ansx+2

        return min(longest(hBars), longest(vBars))**2