# Last updated: 22/7/2026, 5:56:15 p.m.
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0
        
        num = str(n)
        x = []
        summ = 0

        for digit in num:
            if digit != '0':
                x.append(digit)
                summ += int(digit)

        return int(''.join(x))*summ