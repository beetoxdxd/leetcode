# Last updated: 22/7/2026, 5:56:42 p.m.
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        is_increasing = None
        trionic_state, sum_updown, sum_trionic = 0,0,0
        ans = -math.inf

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:  # decreasing
                if is_increasing: trionic_state = 1
                is_increasing = False
            elif nums[i] > nums[i-1]: # increasing
                if trionic_state == 1: trionic_state, sum_trionic, sum_updown = 2, sum_updown, 0
                is_increasing = True
            else: 
                sum_updown, sum_trionic, trionic_state = 0,0,0
                is_increasing = None
                continue

            if is_increasing:
                if trionic_state == 2: 
                    sum_trionic += nums[i-1]
                    ans = max(sum_trionic + nums[i], ans)
                sum_updown = max(nums[i-1], sum_updown + nums[i-1])
            else: sum_updown += nums[i-1]

        return ans