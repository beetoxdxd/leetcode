# Last updated: 22/7/2026, 5:56:29 p.m.
class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        def minimum(row: List[int]) -> tuple:
            first = second = math.inf

            for i in range(len(row)):
                if row[i] < first:
                    second = first
                    first = row[i]
                elif row[i] < second:
                    second = row[i]

            return (first, second)
        m = len(units)
        n = len(units[0])

        if n == 1: return sum(row[0] for row in units)
        if m == 1: return min(units[0])

        global_min = math.inf
        second_min = math.inf
        second_sum = 0
        
        for row in units:
            first, second = minimum(row)
            global_min = min(global_min, first)
            second_min = min(second_min, second)
            second_sum += second

        return second_sum - second_min + global_min