# Last updated: 4/10/2026, 5:53:05 p.m.
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        stack = []
4        cont = []     
5
6        for i, char in enumerate(s):
7            if char == '(':
8                stack.append(i)
9                continue
10
11            if char == '*':
12                cont.append(i)
13                continue
14
15            # )
16            if stack: stack.pop()
17            elif cont: cont.pop()
18            else: return False
19
20        while stack and cont:
21            if stack.pop() > cont.pop(): return False
22
23        return not stack