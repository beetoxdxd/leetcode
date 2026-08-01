# Last updated: 1/8/2026, 5:22:07 p.m.
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, ans = 0, math.inf

        for j in range(k-1, len(nums)):
            diff = nums[j] - nums[i]
            ans = min(ans, diff)
            i += 1

        return ans