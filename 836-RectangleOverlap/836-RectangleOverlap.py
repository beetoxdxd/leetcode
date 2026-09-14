# Last updated: 14/9/2026, 1:21:37 a.m.
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        x1, y1, x2, y2 = rec1
4        x3, y3, x4, y4 = rec2
5
6        if x1 <= x3 < x2 or x1 < x4 <= x2 or x3 <= x1 < x4 or x3 < x2 <= x4:
7            if y1 <= y3 < y2 or y1 < y4 <= y2 or y3 <= y1 < y4 or y3 < y2 <= y4: return True
8            return False
9
10        return False