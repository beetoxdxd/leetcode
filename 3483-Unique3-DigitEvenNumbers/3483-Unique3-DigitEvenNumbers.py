# Last updated: 10/9/2026, 11:07:32 p.m.
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        n = len(digits)
4        vis = [False] * 1000
5        ans = 0
6
7        for i in range(n):
8            if digits[i] == 0:
9                continue
10            for j in range(n):
11                if j == i:
12                    continue
13                for k in range(n):
14                    if k == i or k == j or digits[k] % 2 != 0:
15                        continue
16                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
17                    if not vis[x]:
18                        vis[x] = True
19                        ans += 1
20
21        return ans