# Last updated: 26/10/2026, 12:13:52 a.m.
1class Solution:
2    def minSwaps(self, nums: List[int]) -> int:
3        n = len(nums)
4        digitSum = [0] * n
5        for i, v in enumerate(nums):
6            s = 0
7            while v > 0:
8                s += v % 10
9                v //= 10
10            digitSum[i] = s
11
12        indices = list(range(n))
13        indices.sort(key=lambda i: (digitSum[i], nums[i]))
14
15        targetPos = [0] * n
16        for pos, idx in enumerate(indices):
17            targetPos[idx] = pos
18
19        visited = [False] * n
20        cycles = 0
21        for i in range(n):
22            if not visited[i]:
23                cycles += 1
24                j = i
25                while not visited[j]:
26                    visited[j] = True
27                    j = targetPos[j]
28
29        return n - cycles