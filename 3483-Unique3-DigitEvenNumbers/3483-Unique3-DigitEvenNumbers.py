# Last updated: 10/9/2026, 10:54:33 p.m.
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        cont = Counter(digits)
4        ans = 0
5
6        for num in range(100, 1000, 2):
7            h = defaultdict(int)
8            while num > 0:
9                h[num % 10] += 1
10                num //= 10
11
12            flag = True
13            for key, value in h.items():
14                if value > cont[key]: flag = False
15
16            if flag: ans += 1
17
18        return ans