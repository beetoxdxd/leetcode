# Last updated: 1/8/2026, 5:23:46 p.m.
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        j = 1

        while j < n and prices[j] > prices[0]: j += 1
        if j == n: j = 0

        for i in range(n):
            if i == j or prices[i] > prices[j]:
                j = i+1
                while j < n and prices[j] > prices[i]: j += 1
                if j == n: j = i+1; continue

            prices[i] -= prices[j]

        return prices