# Last updated: 30/8/2026, 11:31:52 p.m.
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        ans = 0
        mod = 10**9 + 7
        
        for num in nums:
            width = num % 10
            d = str(num // 10)

            x = int(d[:width], 10)
            y = int(d[width:], 10)

            ans = (ans + pow(x, y, mod)) % mod

        return int(ans)