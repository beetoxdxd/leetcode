# Last updated: 22/7/2026, 5:57:07 p.m.
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        while True:
            min_sum = math.inf
            index = 0
            is_sorted = True
            
            for i in range(len(nums)-1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum: 
                    min_sum = current_sum
                    index = i
                if nums[i] > nums[i+1]: is_sorted = False

            if is_sorted: break
            nums[index] = min_sum
            nums.pop(index+1)
            ans += 1

        return ans