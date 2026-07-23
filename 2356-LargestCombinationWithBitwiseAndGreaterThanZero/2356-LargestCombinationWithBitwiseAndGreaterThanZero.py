# Last updated: 22/7/2026, 11:36:05 p.m.
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        h = [0] * 24

        for i in range(24):
            for candidate in candidates:
                if candidate & (1 << i): h[i] += 1
        return max(h)