# Last updated: 13/10/2026, 11:25:12 p.m.
1class Solution:
2    def maxSumOfSquares(self, num: int, summ: int) -> str:
3        if summ > 9*num: return ''
4
5        q, r = divmod(summ, 9)
6        ans = '9' * q
7
8        if r > 0: ans += str(r)
9        return ans + ('0' * (num - len(ans)))