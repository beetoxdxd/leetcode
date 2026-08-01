# Last updated: 1/8/2026, 5:22:10 p.m.
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        for i in range(len(nums)):
            ans += '0' if nums[i][i] == '1' else '1'
            
        return ans
