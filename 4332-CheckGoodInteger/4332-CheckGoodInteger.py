# Last updated: 22/7/2026, 5:56:05 p.m.
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squareSum = 0
        digitSum = 0
        
        while n > 0:
            digit = n % 10
            squareSum += digit**2
            digitSum += digit
            n //= 10

        return squareSum - digitSum >= 50