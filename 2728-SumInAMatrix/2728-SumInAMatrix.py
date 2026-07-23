# Last updated: 22/7/2026, 11:35:48 p.m.
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        m = len(nums[0])
        aux = [sorted(row, reverse=True) for row in nums]

        ans = 0
        for j in range(m):
            col = [aux[i][j] for i in range(n)]
            ans += max(col)
        return ans