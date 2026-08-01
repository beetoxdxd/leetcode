# Last updated: 1/8/2026, 5:24:46 p.m.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum1 = 0
        if start > destination: start, destination = destination, start
        
        for i in range(start, destination):
            sum1 += distance[i]

        n = len(distance)
        sum2 = 0
        while destination != start:
            sum2 += distance[destination]

            if destination == n-1: destination = 0
            else: destination += 1

        return min(sum1,sum2)