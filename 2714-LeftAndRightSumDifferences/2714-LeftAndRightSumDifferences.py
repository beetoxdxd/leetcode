# Last updated: 22/7/2026, 11:35:50 p.m.
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightSum = [0]*n

        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        ans = [rightSum[0]]
        aux = 0
        for i in range(1, n):
            aux += nums[i-1]
            ans.append(abs(aux - rightSum[i]))

        return ans