# Last updated: 1/8/2026, 5:23:53 p.m.
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = -math.inf
        for i, num in enumerate(nums):
            if num == 0: continue
            if i - start <= k: return False
            start = i

        return True
