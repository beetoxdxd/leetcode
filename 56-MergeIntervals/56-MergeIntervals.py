# Last updated: 1/8/2026, 5:28:15 p.m.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        interval = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= interval[1]: 
                if current[1] > interval[1]: interval[1] = current[1]
            else:
                ans.append(interval)
                interval = current

        ans.append(interval)
        return ans