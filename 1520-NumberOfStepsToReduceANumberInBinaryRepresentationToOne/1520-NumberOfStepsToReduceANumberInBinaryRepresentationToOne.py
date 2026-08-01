# Last updated: 1/8/2026, 5:24:00 p.m.
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        ans = 0

        while num != 1:
            if num % 2: num += 1
            else: num >>= 1

            ans += 1
        return ans