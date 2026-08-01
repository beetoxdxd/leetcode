# Last updated: 1/8/2026, 5:22:33 p.m.
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = math.inf

        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))

        return ans