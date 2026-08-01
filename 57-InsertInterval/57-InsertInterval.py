# Last updated: 1/8/2026, 5:28:13 p.m.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        new_start, new_end = newInterval
        ans = []
        looking = False
        done = False

        if new_start < intervals[0][0] and new_end < intervals[0][0]: ans.append(newInterval); done = True
        elif new_start < intervals[0][0]: ans_start = new_start; looking = True
        
        for start, end in intervals:
            if start <= new_start <= end:
                looking = True # flag to search for the end
                ans_start = min(start, new_start)
                if start <= new_end <= end: looking = False
                if not looking: ans.append([ans_start, max(end, new_end)]); done = True
            elif looking:
                if start <= new_end <= end: 
                    ans.append([ans_start, max(end, new_end)]); looking = False; done = True
                elif new_end < start: 
                    ans.append([ans_start, new_end]); ans.append([start, end]); looking = False; done = True
            elif start <= new_end <= end: ans.append([new_start, max(end, new_end)]); done = True
            elif not done and new_start < start: 
                if new_end < start: ans.append([new_start, new_end]); ans.append([start, end]); done = True
                else: ans_start = new_start; looking = True
            else: ans.append([start, end])

        if looking: ans.append([ans_start, new_end])
        if new_start > ans[-1][0] and new_end > ans[-1][1]: ans.append(newInterval)

        return ans
