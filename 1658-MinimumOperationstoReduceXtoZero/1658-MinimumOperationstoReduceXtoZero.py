# Last updated: 22/9/2026, 11:00:45 p.m.
1class Solution:
2    def minOperations(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4        k = sum(nums) - x
5        curr, ans = 0, 0
6        i, j = 0, 0
7
8        if k == 0: return n
9
10        while i < n:
11            curr += nums[i]
12
13            while curr > k and j < i: 
14                curr -= nums[j]
15                j += 1
16
17            if curr == k: ans = max(ans, i-j+1)
18            i += 1
19
20        return n - ans if ans else -1