# Last updated: 22/7/2026, 11:36:14 p.m.
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = 0
        beams = 0
        for row in bank:
            current_devices = row.count('1')
            if current_devices > 0: 
                if devices > 0: beams += devices * current_devices
                devices = current_devices
        return beams