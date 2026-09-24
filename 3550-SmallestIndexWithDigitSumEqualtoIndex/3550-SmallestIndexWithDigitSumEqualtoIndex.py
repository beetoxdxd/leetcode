# Last updated: 23/9/2026, 10:07:41 p.m.
1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        def sum_digits(n: int) -> int:
4            summ = 0
5            while n > 0:
6                summ += n % 10
7                n //= 10
8
9            return summ
10
11        for i, num in enumerate(nums):
12            if sum_digits(num) == i: return i
13
14        return -1