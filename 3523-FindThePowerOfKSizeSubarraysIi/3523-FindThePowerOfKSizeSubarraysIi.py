# Last updated: 22/7/2026, 11:35:10 p.m.
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        streak = 1
        ans = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1: streak += 1
            else: streak = 1

            if i < k-1: continue
            if streak >= k: ans.append(nums[i])
            else: ans.append(-1)
            
        return ans