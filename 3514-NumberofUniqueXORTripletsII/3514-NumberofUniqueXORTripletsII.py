# Last updated: 24/7/2026, 1:39:40 a.m.
1class Solution:
2    def uniqueXorTriplets(self, nums: List[int]) -> int:
3        unique_nums = set(nums)
4        pairs = {a ^ b for a in unique_nums for b in unique_nums}
5        triplets = {p ^ c for p in pairs for c in unique_nums}
6
7        return len(triplets)