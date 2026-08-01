# Last updated: 1/8/2026, 5:28:04 p.m.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for digit in digits:
            number = number*10 + digit

        ans = []
        number += 1
        while number > 0:
            ans.append(number % 10)
            number //= 10

        return ans[::-1]