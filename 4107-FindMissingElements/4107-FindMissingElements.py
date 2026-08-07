# Last updated: 7/8/2026, 5:46:57 p.m.
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        expected = nums[0]

        for num in nums:
            if num != expected:
                ans.extend([i for i in range(expected, num)])
            
            expected = num + 1

        return ans