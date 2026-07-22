# Last updated: 22/7/2026, 5:56:04 p.m.
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odds = 0
        even = 0

        for num in nums:
            if num%2: odds +=1
            else: even +=1

        ans = []
        for num in nums:
            if num%2:
                odds -=1
                ans.append(even)
            else:
                even -=1
                ans.append(odds)

        return ans