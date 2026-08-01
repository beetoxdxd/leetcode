# Last updated: 1/8/2026, 5:24:37 p.m.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for elem in arr:
            if elem in d: d[elem] += 1
            else: d[elem] = 1

        l = list(d.values())
        l.sort()
        for i in range(1, len(l)):
            if l[i] == l[i-1]: return False
        return True