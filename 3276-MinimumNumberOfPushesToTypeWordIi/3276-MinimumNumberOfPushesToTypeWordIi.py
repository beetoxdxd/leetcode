# Last updated: 1/8/2026, 5:20:49 p.m.
class Solution:
    def minimumPushes(self, word: str) -> int:
        keys = [1]*8
        i, ans = 0, 0

        for elem in sorted(list(Counter(word).values()), reverse= True):
            if elem == 0: break
            ans += elem*keys[i]
            keys[i] += 1
            i = (i+1) % 8

        return ans