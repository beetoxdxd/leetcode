# Last updated: 1/8/2026, 5:26:44 p.m.
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(i: int, j: int) -> int:
            if i == j: return nums[i]
            return max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))

        return dp(0, len(nums)-1) >= 0