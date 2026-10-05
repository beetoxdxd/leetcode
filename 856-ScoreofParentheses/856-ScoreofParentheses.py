# Last updated: 5/10/2026, 1:42:44 a.m.
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        def traverse(seq: str):
4            n = len(seq)
5            if n < 2: return 0
6            if n == 2: return 1
7
8            stack = []
9            i = 0
10
11            while i < n:
12                if seq[i] == '(': stack.append(i)
13                else: stack.pop()
14
15                i += 1
16                if not stack: break
17
18            aux = traverse(seq[1:i-1])
19            acc = 2*aux if aux >= 1 else 1
20            acc += traverse(seq[i:])
21            return acc
22
23        return traverse(s)