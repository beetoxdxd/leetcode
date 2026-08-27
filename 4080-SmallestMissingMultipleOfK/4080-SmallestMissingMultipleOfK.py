# Last updated: 27/8/2026, 4:57:15 p.m.
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        divisible = set()

        for num in nums:
            if num % k == 0: divisible.add(num)

        mult = 1
        while k * mult in divisible: mult += 1

        return k*mult