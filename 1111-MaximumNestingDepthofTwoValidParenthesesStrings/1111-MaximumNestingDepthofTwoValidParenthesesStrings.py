# Last updated: 29/9/2026, 10:20:00 p.m.
1class Solution:
2    def maxDepthAfterSplit(self, seq: str) -> list[int]:
3        par = 0
4        nested = 0
5
6        for char in seq:
7            if char == '(': par += 1
8            elif char == ')': par -= 1
9
10            nested = max(nested, par)
11
12        max_depth = nested//2
13        ans = [0] * len(seq)
14        stack = []
15
16        for i, char in enumerate(seq):
17            if char == '(': stack.append(i)
18            else: 
19                index = stack.pop()
20                if len(stack) < max_depth: 
21                    ans[index] = ans[i] = 1
22
23        return ans