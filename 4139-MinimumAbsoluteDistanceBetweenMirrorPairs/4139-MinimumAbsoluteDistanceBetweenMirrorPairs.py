# Last updated: 22/7/2026, 5:56:13 p.m.
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        h = {}
        h[int(str(nums[0])[::-1])] = 0
        n = len(nums)
        ans = n

        for i in range(1, n):            
            if nums[i] in h: ans = min(ans, i - h[nums[i]])

            if ans == 1: return 1
            h[int(str(nums[i])[::-1])] = i

        return ans if ans != n else -1