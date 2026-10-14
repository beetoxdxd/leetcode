# Last updated: 13/10/2026, 11:22:37 p.m.
1class Solution:
2    def maxSumOfSquares(self, num: int, summ: int) -> str:
3        ans = []
4        while num and summ:
5            if summ > 9: ans.append('9')
6            else: ans.append(str(summ))
7
8            num -= 1
9            summ -= int(ans[-1])
10
11        return '' if summ else ''.join(ans) + '0'*num