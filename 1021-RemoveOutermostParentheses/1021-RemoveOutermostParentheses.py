# Last updated: 7/10/2026, 10:11:41 p.m.
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        stack = 0
4        aux = []
5        chunk = 1
6
7        for i, char in enumerate(s):
8            if char == '(': stack += 1
9            else: stack -= 1
10
11            if stack == 0:
12                aux.append(''.join(s[chunk:i]))
13                chunk = i+2
14
15        return ''.join(aux)