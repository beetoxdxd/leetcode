# Last updated: 22/7/2026, 11:36:11 p.m.
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        times_pivot = 0

        for num in nums:
            if num < pivot: before.append(num)
            elif num > pivot: after.append(num)
            else: times_pivot += 1

        return before + [pivot]*times_pivot + after