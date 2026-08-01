# Last updated: 1/8/2026, 5:26:26 p.m.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h = defaultdict(bool)
        repeated = 0
        for n in nums:
            if h[n] == True: repeated = n
            h[n] = True
        
        for i in range(1, len(nums)+1):
            if h[i] is False: return [repeated, i]

        