# Last updated: 1/8/2026, 5:26:32 p.m.
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= 0 or nums[-1] < 0: return nums[-1]*nums[-2]*nums[-3]

        aux = nums[0] * nums[1]
        aux2 = nums[-1]*nums[-2]
        if aux > 0 and aux > aux2: return aux * nums[-1]

        return max(aux2*nums[-3], aux*nums[-1])