# Last updated: 22/7/2026, 5:56:20 p.m.
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            cont = 0

            for j in range(i, n):
                if nums[j] == target: cont += 1
                if cont > (j-i+1)//2: ans += 1

        return ans