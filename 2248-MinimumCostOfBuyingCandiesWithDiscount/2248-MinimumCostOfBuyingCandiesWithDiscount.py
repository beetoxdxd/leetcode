# Last updated: 22/7/2026, 11:36:12 p.m.
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0

        while cost:
            ans += cost.pop()
            if cost: ans += cost.pop()
            if cost: cost.pop()

        return ans