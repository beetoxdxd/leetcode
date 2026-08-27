# Last updated: 27/8/2026, 5:00:02 p.m.
class Solution:
    def sumGame(self, num: str) -> bool:
        sum_first, sum_second = 0, 0
        op_first, op_second = 0, 0
        n = len(num)

        for i in range(n // 2):
            if num[i] == '?': op_first += 1
            else: sum_first += ord(num[i]) - ord('0')

        for i in range(n // 2, n):
            if num[i] == '?': op_second += 1
            else: sum_second += ord(num[i]) - ord('0')

        while op_second and op_first:
            op_second -= 1
            op_first -= 1

        if op_second == 0 and op_first == 0: return sum_second != sum_first
        if (op_first + op_second) % 2 == 1: return True
        if op_second: return sum_second + 9*(op_second//2) != sum_first
        return sum_first + 9*(op_first//2) != sum_second