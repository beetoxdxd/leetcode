# Last updated: 1/8/2026, 5:25:56 p.m.
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        primes = {2,3,5,7,11,13,17,19,23,29}
        for num in range(left, right+1):
            if bin(num).count('1') in primes: ans += 1

        return ans