# Last updated: 22/7/2026, 11:35:27 p.m.
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        u = min(nums[1], nums[2])
        v = max(nums[2], nums[1])

        for i in range(3, len(nums)):
            if nums[i] < u:
                v, u = u, nums[i]
            elif nums[i] < v:
                v = nums[i]

        return nums[0] + u + v