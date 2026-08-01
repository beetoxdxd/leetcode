# Last updated: 1/8/2026, 5:22:46 p.m.
class Solution:
    def minOperations(self, s: str) -> int:
        op1 = '1'
        op2 = '0'
        ans1 = ans2 = 0

        for i in range(len(s)):
            if s[i] != op1: ans1 += 1
            if s[i] != op2: ans2 += 1

            op1 = '0' if op1 == '1' else '1'
            op2 = '0' if op2 == '1' else '1'
        
        return min(ans1, ans2)