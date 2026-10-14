# Last updated: 13/10/2026, 11:23:29 p.m.
1class Solution:
2    def maxSumOfSquares(self, num: int, summ: int) -> str:
3        if summ > 9*num: return ''
4
5        ans = []
6        while num and summ:
7            if summ > 9: ans.append('9')
8            else: ans.append(str(summ))
9
10            num -= 1
11            summ -= int(ans[-1])
12
13        return ''.join(ans) + '0'*num