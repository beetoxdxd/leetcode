# Last updated: 1/8/2026, 5:23:43 p.m.
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans