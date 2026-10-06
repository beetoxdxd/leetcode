# Last updated: 5/10/2026, 11:35:27 p.m.
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        stack = 0
4        cont = 0
5
6        for char in s:
7            if char == '(': stack += 1
8            elif stack: stack -= 1
9            else: cont += 1
10
11        return cont + stack