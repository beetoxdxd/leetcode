# Last updated: 28/9/2026, 11:02:35 p.m.
1class Solution:
2    def braceExpansionII(self, expression: str) -> List[str]:
3        idx = 0
4        n = len(expression)
5
6        def is_letter(c: str) -> bool:
7            return "a" <= c <= "z"
8
9        # Recursive descent parser
10        def expr() -> set:
11            nonlocal idx
12            ret = set()
13            while True:
14                # Take the union with the result of term()
15                ret |= term()
16                # Continue if a comma is matched; otherwise, stop matching
17                if idx < n and expression[idx] == ",":
18                    idx += 1
19                    continue
20                else:
21                    break
22            return ret
23
24        # term -> item | item term
25        def term() -> set:
26            nonlocal idx
27            # Initialize an empty set and take its Cartesian product with subsequent results
28            ret = {""}
29            # An item starts with { or a lowercase letter; continue matching only when this condition is met
30            while idx < n and (
31                expression[idx] == "{" or is_letter(expression[idx])
32            ):
33                sub = item()
34                tmp = set()
35                for left in ret:
36                    for right in sub:
37                        tmp.add(left + right)
38                ret = tmp
39            return ret
40
41        # item -> letter | { expr }
42        def item() -> set:
43            nonlocal idx
44            ret = set()
45            if expression[idx] == "{":
46                idx += 1
47                ret = expr()
48            else:
49                ret = {expression[idx]}
50            idx += 1
51            return ret
52
53        ret = expr()
54        return sorted(list(ret))