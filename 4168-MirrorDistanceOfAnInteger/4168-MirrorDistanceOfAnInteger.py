# Last updated: 22/7/2026, 5:56:12 p.m.
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))