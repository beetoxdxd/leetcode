# Last updated: 7/8/2026, 5:46:45 p.m.
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        valid = 0
        
        for i in range(n):
            even, odd = 0, 0
            
            for j in range(i, n):
                if nums[j] % 2: odd += 1
                else: even += 1

                if odd > 0 and even / odd <= a / b: valid += 1

        return valid