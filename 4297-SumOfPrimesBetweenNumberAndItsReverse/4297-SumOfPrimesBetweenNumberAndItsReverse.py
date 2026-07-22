# Last updated: 22/7/2026, 5:56:06 p.m.
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def prime(n: int) -> int:
            if n <= 1: return 0
            if n == 2: return 2
            if n % 2 == 0: return 0

            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0: return 0

            return n

            
        reverse = int(str(n)[::-1])
        x, y = min(n, reverse), max(n, reverse)
        ans = 0

        for i in range(x, y+1):
            ans += prime(i)

        return ans