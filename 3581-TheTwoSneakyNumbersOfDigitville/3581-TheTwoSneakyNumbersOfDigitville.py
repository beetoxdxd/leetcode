# Last updated: 22/7/2026, 11:35:08 p.m.
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []

        for num in nums:
            if num in d: ans.append(num)
            else: d[num] = 1

        return ans