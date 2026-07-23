# Last updated: 22/7/2026, 11:36:09 p.m.
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return 0 if num1 == 0 or num2 == 0 else num1//num2 + self.countOperations(num2, num1%num2)