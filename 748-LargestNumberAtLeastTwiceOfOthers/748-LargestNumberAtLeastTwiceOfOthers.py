# Last updated: 1/8/2026, 5:26:03 p.m.
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second = max(nums[0], nums[1]), min(nums[0], nums[1])
        index = 0 if largest == nums[0] else 1

        for i in range(2, len(nums)):
            if nums[i] > largest: 
                second, largest = largest, nums[i]
                index = i
            elif nums[i] > second: second = nums[i]

        return index if second*2 <= largest else -1