# Last updated: 1/8/2026, 5:23:26 p.m.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        i = 1
        n = len(colors)
        cont = 0

        while i < n:
            if colors[i] == colors[i-1]:
                index = i-1
                start = i-1
                while i < n and colors[i] == colors[i-1]:
                    if neededTime[index] < neededTime[i]: index = i
                    i += 1
                for j in range(start, i):
                    if j != index: cont += neededTime[j]
            i += 1

        return cont