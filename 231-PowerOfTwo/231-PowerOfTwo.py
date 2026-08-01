# Last updated: 1/8/2026, 5:27:16 p.m.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1