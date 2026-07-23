# Last updated: 22/7/2026, 11:35:13 p.m.
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        zero = False
        ans = 0
        for num in s:
            if num == '0': 
                zero = True 
                continue
            
            ones += 1
            if zero: 
                ans += ones-1
                zero = False

        if zero: ans += ones
        return ans