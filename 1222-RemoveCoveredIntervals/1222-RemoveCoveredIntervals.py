# Last updated: 1/8/2026, 5:24:58 p.m.
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse = True, key = lambda x: x[1])
        intervals.sort(key = lambda x: x[0])
        ans = n = len(intervals)
        max_end = intervals[0][1]

        for i in range(1, n):
            a, b = intervals[i]

            if b <= max_end: ans -= 1
            else: max_end = b

        return ans