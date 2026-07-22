# Last updated: 22/7/2026, 5:57:10 p.m.
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        size = len(s)
        l = list(s)
        while size > 2:
            for i in range(size-1): l[i] = str((int(l[i]) + int(l[i+1])) % 10)
            size -= 1
        return True if l[0] == l[i] else False