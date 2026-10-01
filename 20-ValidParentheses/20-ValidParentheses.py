# Last updated: 30/9/2026, 10:57:08 p.m.
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4
5        for char in s:
6            if char in '([{': stack.append(char)
7            else:
8                if not stack: return False
9                x = stack.pop()
10                if x == '(' and char != ')': return False
11                if x == '[' and char != ']': return False
12                if x == '{' and char != '}': return False
13
14        return False if stack else True