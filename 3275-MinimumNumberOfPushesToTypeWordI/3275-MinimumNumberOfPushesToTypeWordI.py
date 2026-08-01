# Last updated: 1/8/2026, 5:20:51 p.m.
class Solution:
    def minimumPushes(self, word: str) -> int:
        h = [1] * 8
        i = 0
        ans = 0

        for char in word:
            ans += h[i]
            h[i] += 1

            i = (i+1) % 8

        return ans