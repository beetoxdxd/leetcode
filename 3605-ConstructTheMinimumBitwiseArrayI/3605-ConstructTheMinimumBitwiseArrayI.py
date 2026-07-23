# Last updated: 22/7/2026, 11:35:04 p.m.
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for j, num in enumerate(nums):
            if num == 2:
                ans.append(-1)
                continue

            ones = 1
            while (num >> ones) & 1:
                ones += 1

            ans.append(num - (1 << (ones-1)))

        return ans