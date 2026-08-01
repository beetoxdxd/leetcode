# Last updated: 1/8/2026, 5:29:32 p.m.
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == " ": i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-': sign = 0
            i += 1


        bound = int(math.pow(2,31))
        ans = 0
        while i < n and s[i] >= '0' and s[i] <= '9':
            ans = ans*10 + int(s[i])
            i += 1

            if ans > bound-1 and sign: return bound-1
            if ans > bound and not sign: return -bound

        return ans if sign else -ans