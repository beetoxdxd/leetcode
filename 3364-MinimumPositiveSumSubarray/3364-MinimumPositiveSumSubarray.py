# Last updated: 15/11/2026, 12:02:31 a.m.
1class Solution:
2    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
3        n = len(nums)
4        prefix = [0] * (n + 1)
5        for i in range(n):
6            prefix[i + 1] = prefix[i] + nums[i]
7
8        best = float('inf')
9        for length in range(l, r + 1):
10            for i in range(n - length + 1):
11                s = prefix[i + length] - prefix[i]
12                if 0 < s < best:
13                    best = s
14
15        return -1 if best == float('inf') else best