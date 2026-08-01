# Last updated: 1/8/2026, 5:22:55 p.m.
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cont = 0
        ans = 0
        for n in gain:
            cont += n
            ans = max(ans, cont)

        return ans