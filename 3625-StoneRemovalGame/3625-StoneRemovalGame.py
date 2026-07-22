# Last updated: 22/7/2026, 5:57:18 p.m.
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1

        return True if stones % 2 else False