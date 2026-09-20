# Last updated: 19/9/2026, 9:15:22 p.m.
1class Solution:
2    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
3        ans = 0
4        n = len(intervals)
5        
6        for i in range(n):
7            a, b = intervals[i]
8            for j in range(i+1, n):
9                x, y = intervals[j]
10
11                if x <= b <= y or x <= a <= y or a <= x <= b or a <= y <= b: ans += 1
12
13        return ans