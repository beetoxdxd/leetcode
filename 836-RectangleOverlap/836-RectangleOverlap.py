# Last updated: 14/9/2026, 1:26:59 a.m.
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        x1, y1, x2, y2 = rec1
4        x3, y3, x4, y4 = rec2
5
6        return not(x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)