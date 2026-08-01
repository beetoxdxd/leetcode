# Last updated: 1/8/2026, 5:28:58 p.m.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        i = 0
        aux = []
        while i < len(nums):
            if nums[i] == val:
                aux.append(nums.pop(i))
            else:
                ans += 1
                i += 1
            
        return ans