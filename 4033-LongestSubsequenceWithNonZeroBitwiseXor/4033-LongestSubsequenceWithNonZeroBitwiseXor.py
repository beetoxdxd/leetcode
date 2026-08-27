# Last updated: 27/8/2026, 4:57:22 p.m.
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        totalXor = 0
        allZero = True

        for x in nums:
            totalXor ^= x
            if x > 0:
                allZero = False

        if totalXor > 0:
            return n
        return n - 1 if allZero == False else 0