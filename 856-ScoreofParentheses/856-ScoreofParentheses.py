# Last updated: 5/10/2026, 1:46:52 a.m.
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        score = 0
4        depth = 0
5
6        for i, char in enumerate(s):
7            if char == '(':
8                depth += 1
9            else:
10                depth -= 1
11                # Solo sumamos cuando encontramos un "()" interior
12                if s[i - 1] == '(':
13                    score += 1 << depth  # Equivale a 2 ** depth
14
15        return score