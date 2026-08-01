# Last updated: 1/8/2026, 5:24:04 p.m.
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        occurrences = [0]*101

        for n in nums:
            occurrences[n] += 1
        
        acc = 0
        smaller = [0]*101
        for i in range(101):
            smaller[i] = acc
            acc += occurrences[i]
        
        ans = []
        for n in nums:
            ans.append(smaller[n])

        return ans