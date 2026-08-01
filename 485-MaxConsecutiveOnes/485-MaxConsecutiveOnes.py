# Last updated: 1/8/2026, 5:26:46 p.m.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        consecutive = 0
        for n in nums:
            if n == 1: consecutive += 1
            else:
                if consecutive > m: m = consecutive
                consecutive = 0
        return m if m > consecutive else consecutive