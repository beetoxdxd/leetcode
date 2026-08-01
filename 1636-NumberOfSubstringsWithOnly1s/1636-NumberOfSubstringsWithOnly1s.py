# Last updated: 1/8/2026, 5:23:35 p.m.
class Solution:
    def numSub(self, s: str) -> int:
        ones = 0
        ans = 0
        for char in s:
            if char == '1': 
                ones += 1
                ans += ones
            else:
                ones = 0

        return ans % (10**9 + 7)