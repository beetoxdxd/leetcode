# Last updated: 1/8/2026, 5:26:37 p.m.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0

        for num in set(nums):
            if num+1 in counts: ans = max(ans, counts[num] + counts[num+1])

        return ans