# Last updated: 7/10/2026, 10:06:17 p.m.
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        stack = 0
4        aux = []
5        chunk = []
6
7        for char in s:
8            chunk.append(char)
9
10            if char == '(': stack += 1
11            else: stack -= 1
12
13            if stack == 0:
14                aux.append(''.join(chunk[1:-1]))
15                chunk = []
16
17        return ''.join(aux)