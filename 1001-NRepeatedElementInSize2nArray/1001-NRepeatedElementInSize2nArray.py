# Last updated: 1/8/2026, 5:25:18 p.m.
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        h = []

        for num in nums:
            if num in h: return num

            h.append(num)

        