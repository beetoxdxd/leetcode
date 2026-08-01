# Last updated: 1/8/2026, 5:22:39 p.m.
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        limit = 10**5 + 1
        h = [0] * limit
        ans = 0

        for cost in costs:
            h[cost] += 1

        for i in range(limit):
            for j in range(h[i]):
                if coins < i: return ans
                coins -= i
                ans += 1
            
        return ans