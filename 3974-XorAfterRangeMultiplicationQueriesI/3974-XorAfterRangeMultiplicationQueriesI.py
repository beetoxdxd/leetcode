# Last updated: 22/7/2026, 5:56:35 p.m.
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7

        for query in queries:
            idx, r, k, v = query

            while idx <= r:
                nums[idx] = (nums[idx] * v) % mod
                idx += k

        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]

        return ans