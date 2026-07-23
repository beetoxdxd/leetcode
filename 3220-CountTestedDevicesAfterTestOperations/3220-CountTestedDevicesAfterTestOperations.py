# Last updated: 22/7/2026, 11:35:32 p.m.
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        devices = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - devices > 0: devices += 1
        return devices