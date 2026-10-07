# Last updated: 6/10/2026, 10:50:28 p.m.
1class Solution:  # Iterative
2    def removeInvalidParentheses(self, s: str) -> List[str]:
3        res = []
4        stack = [(s, 0, 0, ("(", ")"))]
5
6        while stack:
7            cur, li, lj, par = stack.pop()
8            n = len(cur)
9            bal = 0
10            match = False
11
12            for i in range(li, n):
13                bal += (cur[i] == par[0]) - (cur[i] == par[1])
14                if bal >= 0:
15                    continue
16
17                for j in range(lj, i + 1):
18                    if cur[j] == par[1] and (j == lj or cur[j - 1] != par[1]):
19                        nxt = cur[:j] + cur[j + 1 :]
20                        stack.append((nxt, i, j, par))
21
22                match = True
23                break
24
25            if not match:
26                rev = cur[::-1]
27
28                if par[0] == "(":
29                    stack.append((rev, 0, 0, (")", "(")))
30                else:
31                    res.append(rev)
32
33        return res