# Last updated: 1/8/2026, 5:27:46 p.m.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0
        maxSoFar = 0

        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)

        return maxSoFar

