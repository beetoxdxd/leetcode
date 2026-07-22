# Last updated: 22/7/2026, 5:56:25 p.m.
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            even = odd = 0
            h = set()

            for j in range(i, n):
                if nums[j] not in h:
                    h.add(nums[j])
                    if nums[j] % 2 == 0: even += 1
                    else: odd += 1

                if even == odd: ans = max(ans, j - i + 1)

        return ans
