# Last updated: 22/7/2026, 5:56:43 p.m.
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        state = True
        picos = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] or len(picos) > 2: return False
            if state and nums[i] < nums[i-1]: # ascendente
                picos.append(i-1)
                state = False
            elif not state and nums[i] > nums[i-1]: # descendente
                picos.append(i-1)
                state = True

        if len(picos) != 2: return False
        if 0 == picos[0] or picos[1] == len(nums)-1: return False
        return True
