# Last updated: 26/10/2026, 12:29:05 a.m.
1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        happiness.sort()
4        ans, cont = 0, 0
5
6        while happiness and k:
7            child = happiness.pop()
8            if child - cont <= 0: break
9
10            ans += child - cont
11
12            k -= 1
13            cont += 1
14
15        return ans