# Last updated: 22/7/2026, 5:57:20 p.m.
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2:
                ans.append(-1)
                continue
            
            i = 0
            while (num >> i) & 1: i += 1
            ans.append(num - (1 << (i-1)))
        
        return ans