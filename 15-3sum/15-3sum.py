# Last updated: 1/8/2026, 5:29:20 p.m.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            target = -nums[i]
            left, right = i+1, n-1

            while left < right:
                suma = nums[left] + nums[right]
                if suma < target: left += 1
                elif suma > target: right -= 1
                else: 
                    solution.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    right -= 1; left += 1

        return solution