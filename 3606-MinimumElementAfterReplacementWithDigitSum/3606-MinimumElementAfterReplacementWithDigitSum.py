# Last updated: 22/7/2026, 11:35:03 p.m.
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(digit) for digit in str(num)) for num in nums)