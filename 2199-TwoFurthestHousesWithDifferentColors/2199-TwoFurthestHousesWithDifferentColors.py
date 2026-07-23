# Last updated: 22/7/2026, 11:36:20 p.m.
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i, j = 0, n-1

        while i < n and j >= 0:
            if colors[i] != colors[n-1]: return n-1-i
            if colors[j] != colors[0]: return j

            i += 1
            j -= 1

        return 0