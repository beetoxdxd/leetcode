# Last updated: 24/7/2026, 9:54:37 p.m.
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(str(n))
        return int(digits[-1]) * int(digits[-2])