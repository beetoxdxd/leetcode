# Last updated: 23/7/2026, 12:50:16 a.m.
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        pairs = {a ^ b for a in unique_nums for b in unique_nums}
        triplets = {p ^ c for p in pairs for c in unique_nums}

        return len(triplets)