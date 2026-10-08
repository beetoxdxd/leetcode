# Last updated: 7/10/2026, 9:55:47 p.m.
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        stack = []
4        aux = []
5        chunk = []
6
7        for i, char in enumerate(s):
8            chunk.append(char)
9            if char == '(': stack.append(i)
10            else: stack.pop()
11
12            if len(stack) == 0:
13                aux.append(''.join(chunk[1:-1]))
14                chunk = []
15
16        return ''.join(aux)