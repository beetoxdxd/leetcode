# Last updated: 1/8/2026, 5:22:56 p.m.
class Solution:
    def totalMoney(self, n: int) -> int:
        times = n // 7
        dif = 0
        ans = 0
        for i in range(times):
            ans += 28 + dif
            dif += 7
            
        for i in range(times+1, n%7+times+1):
            ans += i

        return ans
