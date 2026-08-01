# Last updated: 1/8/2026, 5:24:49 p.m.
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        h = {}

        def divisors(num: int) -> int:
            sum_divisors = 0
            cont = 0
            for i in range(1, int(math.sqrt(num))+1):
                if cont > 4: return 0
                if num % i == 0: 
                    product = num // i
                    cont += 1
                    sum_divisors += i

                    if i != product:
                        cont += 1
                        sum_divisors += product

            return sum_divisors if cont == 4 else 0

        ans = 0
        for elem in nums:
            if elem not in h: h[elem] = divisors(elem)
            ans += h[elem]

        return ans