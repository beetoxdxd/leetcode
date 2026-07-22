# Last updated: 22/7/2026, 5:57:19 p.m.
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total, left, right = sum(nums), 0, 0
        ans = 0

        for num in nums:
            right = total - left - num
            if num == 0:
                if right == left: ans += 2
                elif right == left +1 or left == right + 1: ans += 1
            left += num
        return ans