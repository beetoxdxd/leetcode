# Last updated: 1/8/2026, 5:28:49 p.m.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        stack = []
        ans = 0

        for i in range(n):
            if s[i] == '(': stack.append(i)
            elif stack:
                index = stack.pop()
                cont = 2 + dp[i] + dp[index]
                dp[i+1] = cont
                if dp[i+1] > ans: ans = dp[i+1]
        
        return ans