# Last updated: 22/7/2026, 5:57:03 p.m.
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        start, end = bounds[0]

        for i in range(1, len(original)):
            gap = original[i] - original[i-1]
            start, end = max(start + gap, bounds[i][0]), min(end + gap, bounds[i][1])
            if end < start: return 0

        return end-start+1