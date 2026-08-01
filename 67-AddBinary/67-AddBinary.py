# Last updated: 1/8/2026, 5:28:02 p.m.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]