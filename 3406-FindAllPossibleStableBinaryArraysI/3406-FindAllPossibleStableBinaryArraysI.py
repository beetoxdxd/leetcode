# Last updated: 22/7/2026, 11:35:20 p.m.
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def traverse(zeros, ones, last):
            if zeros == 0 and ones == 0: return 1

            pos = 0
            if last == 0:
                for k in range(1, min(ones, limit) + 1):
                    pos += traverse(zeros, ones - k, 1)
            else:
                for k in range(1, min(zeros, limit) + 1):
                    pos += traverse(zeros - k, ones, 0)

            return pos % mod

        res_zero = 0
        for k in range(1, min(zero, limit) + 1):
            res_zero = (res_zero + traverse(zero - k, one, 0)) % mod
            
        res_one = 0
        for k in range(1, min(one, limit) + 1):
            res_one = (res_one + traverse(zero, one - k, 1)) % mod
            
        return (res_zero + res_one) % mod