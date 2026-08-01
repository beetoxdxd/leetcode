# Last updated: 1/8/2026, 5:22:11 p.m.
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))