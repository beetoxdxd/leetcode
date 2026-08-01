# Last updated: 1/8/2026, 5:27:04 p.m.
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        ans = [0] * (n+1)
        ans[0] = 0
        ans[1] = 1

        for i in range(2, n+1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans