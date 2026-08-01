# Last updated: 1/8/2026, 5:26:05 p.m.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        index = len(cost)-3
        ans = 0

        while index >= 0:
            cost[index] = min(cost[index]+cost[index+2], cost[index]+cost[index+1])
            index -= 1

        return cost[0] if cost[0] < cost[1] else cost[1]