# Last updated: 8/10/2026, 9:53:47 p.m.
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        ans = 0
4        i = 0
5        n = len(s)
6        stack = []
7
8        while i < n:
9            if s[i] == '(': 
10                stack.append(i)
11                i += 1
12                continue
13
14            if i+1 < n and s[i+1] == ')':
15                if stack: stack.pop()
16                else: ans += 1
17
18                i += 2
19                continue
20
21            if stack: stack.pop()
22            else: ans += 1
23
24            ans += 1
25            i += 1
26
27        return ans + len(stack)*2