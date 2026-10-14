# Last updated: 13/10/2026, 10:58:17 p.m.
1class Solution:
2    def maxSumOfSquares(self, num: int, summ: int) -> str:
3        ans = []
4        while num and summ:
5            if summ > 9: ans.append(9)
6            else: ans.append(summ)
7
8            num -= 1
9            summ -= ans[-1]
10
11        if summ: return ''
12
13        return ''.join(map(str, ans)) + '0'*num