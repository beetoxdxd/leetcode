# Last updated: 1/8/2026, 5:24:44 p.m.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cont = Counter(text)
        return min(cont['b'],cont['a'],cont['l']//2,cont['o']//2,cont['n'])