# Last updated: 1/8/2026, 5:26:33 p.m.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = True
        for i in range(len(flowerbed) - 1):
            if available and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                available = False
                continue

            available = True if flowerbed[i] == 0 else False

        if flowerbed[-1] == 0 and available: n -= 1 
        return True if n <= 0 else False
