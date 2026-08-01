# Last updated: 1/8/2026, 5:24:18 p.m.
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs(30*hour + minutes*0.5 - minutes*6)
        return min(diff, 360-diff)