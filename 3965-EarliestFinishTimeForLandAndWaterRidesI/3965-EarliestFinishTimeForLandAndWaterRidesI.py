# Last updated: 22/7/2026, 5:56:38 p.m.
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        earliest_land = min(start + duration for start,duration in zip(landStartTime, landDuration))
        earliest_water = min(start + duration for start,duration in zip(waterStartTime, waterDuration))

        ans = math.inf
        for i, start in enumerate(waterStartTime):
            if start > earliest_land: ans = min(ans, waterDuration[i] + start)
            else: ans = min(ans, earliest_land + waterDuration[i])

        for i, start in enumerate(landStartTime):
            if start > earliest_water: ans = min(ans, landDuration[i] + start)
            else: ans = min(ans, earliest_water + landDuration[i])

        return ans