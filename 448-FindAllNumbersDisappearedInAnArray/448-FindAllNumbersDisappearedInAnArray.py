# Last updated: 1/8/2026, 5:26:50 p.m.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h = defaultdict(bool)

        for n in nums:
            h[n] = True

        ans = []
        for i in range(1, len(nums)+1):
            if i not in h: ans.append(i)

        return ans 