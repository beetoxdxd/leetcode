# Last updated: 3/10/2026, 4:38:38 p.m.
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        res = 0
4        st = [-1]
5        
6        for i, c in enumerate(s):
7            if c == '(':
8                st.append(i)
9            else:
10                st.pop()
11                
12                if not st:
13                    st.append(i)
14                else:
15                    res = max(res, i - st[-1])
16                    
17        return res