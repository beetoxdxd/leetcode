# Last updated: 23/7/2026, 12:58:10 a.m.
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        return pow(2, int(math.log2(n))+1) if n > 2 else n