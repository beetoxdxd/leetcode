# Last updated: 22/7/2026, 11:35:54 p.m.
class Solution:

    def possible(self, stations: List[int], k: int, value: int, r: int) -> bool:
        i = 0
        size = len(stations)
        adiciones = [0]*size
        boost = 0

        for i in range(size):
            boost += adiciones[i]
            power = stations[i] + boost
            if power < value:
                diff = value - power
                k -= diff
                if k < 0: return False

                boost += diff
                end = i + 2*r + 1
                if end < size: adiciones[end] -= diff
        return True

    def binary(self, stations: List[int], start: int, end: int, k: int, r: int) -> int:
        #print(f"Binary [{start}, {end}]")
        value = None
        while start <= end:
            half = (start+end) // 2
            aux = self.possible(stations, k, half, r)
            if aux:
                value = half
                start = half+1
            else:
                end = half-1

        if value is None: return end
        return value

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        acc = sum(stations[:r+1])
        initial = [acc]
        j = -r

        for i in range(r+1, len(stations)+r):
            if i < len(stations): acc += stations[i]
            if j >= 0: acc -= stations[j]
            initial.append(acc)
            j += 1
        #print(initial)
        return self.binary(initial, min(initial), max(initial)+k, k, r)