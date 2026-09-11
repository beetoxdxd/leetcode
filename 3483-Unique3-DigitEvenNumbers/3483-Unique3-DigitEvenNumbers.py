# Last updated: 10/9/2026, 11:03:22 p.m.
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        cont = defaultdict(int)
4        for digit in digits:
5            cont[str(digit)] += 1
6
7        ans = 0
8
9        for num in range(100, 1000, 2):
10            h = Counter(str(num))
11
12            flag = True
13            for key, value in h.items():
14                if value > cont[key]: flag = False
15
16            if flag: ans += 1
17
18        return ans