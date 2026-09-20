# Last updated: 19/9/2026, 9:28:51 p.m.
1class Solution:
2    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
3        intervals.sort()
4        n = len(intervals)
5        ans = 0
6        
7        for i in range(n):
8            j = bisect.bisect_right(intervals, intervals[i][1], key=lambda x: x[0])
9            ans += j-i-1
10
11        return ans