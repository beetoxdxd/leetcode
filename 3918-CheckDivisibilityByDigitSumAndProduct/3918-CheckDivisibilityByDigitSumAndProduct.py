# Last updated: 27/8/2026, 4:57:40 p.m.
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [ord(char) - ord('0') for char in str(n)]
        digit_sum = 0
        digit_product = 1

        for digit in digits:
            digit_sum += digit
            digit_product *= digit

        return n % (digit_sum + digit_product) == 0