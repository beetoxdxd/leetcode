# Last updated: 5/10/2026, 11:33:29 p.m.
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        stack = []
4        cont = 0
5
6        for i, char in enumerate(s):
7            if char == '(': stack.append(i)
8            else:
9                if stack: stack.pop()
10                else: cont += 1
11
12        return cont + len(stack)