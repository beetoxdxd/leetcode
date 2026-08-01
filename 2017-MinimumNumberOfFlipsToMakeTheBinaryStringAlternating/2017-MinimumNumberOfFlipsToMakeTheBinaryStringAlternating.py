# Last updated: 1/8/2026, 5:22:22 p.m.
class Solution:
    def minFlips(self, s: str) -> int:
        zeros_odd, zeros_even, ones_odd, ones_even = 0,0,0,0
        n = len(s)

        for i in range(n):
            if i % 2: # odd
                if s[i] == '0': zeros_odd += 1
                else: ones_odd += 1
            else:
                if s[i] == '0': zeros_even += 1
                else: ones_even += 1

        if n % 2 == 0: return min(n - (zeros_odd + ones_even), n - (zeros_even + ones_odd))

        ans = math.inf
        for i in range(n):
            zeros_odd, ones_even, zeros_even, ones_odd = zeros_even, ones_odd, zeros_odd, ones_even
            if s[i] == '1': 
                ones_even += 1
                ones_odd -= 1
            else:
                zeros_even += 1
                zeros_odd -= 1

            ans = min(min(n - (zeros_odd + ones_even), n - (zeros_even + ones_odd)), ans)
        
        return ans