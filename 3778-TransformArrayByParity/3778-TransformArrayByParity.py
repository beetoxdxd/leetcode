# Last updated: 22/7/2026, 5:57:05 p.m.
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        odds = 0

        for num in nums:
            if num % 2: odds += 1
            else: even += 1

        ans = []
        for i in range(even):
            ans.append(0)

        for i in range(odds):
            ans.append(1)

        return ans