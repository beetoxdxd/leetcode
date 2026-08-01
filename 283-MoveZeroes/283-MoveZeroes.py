# Last updated: 1/8/2026, 5:27:09 p.m.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cont = 0
        i = 0
        length = len(nums)-1
        while i < length:
            if nums[i] == 0: 
                nums.pop(i)
                cont += 1
                length -= 1
            else: i += 1

        for i in range(cont):
            nums.append(0)
        