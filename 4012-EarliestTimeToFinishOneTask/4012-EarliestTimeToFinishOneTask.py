# Last updated: 22/7/2026, 5:56:26 p.m.
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(start + time for start, time in tasks)