# Last updated: 11/10/2026, 11:11:46 p.m.
1class Solution:
2    def maxSum(self, nums: List[int], k: int) -> int:
3        MOD = 10**9 + 7
4        cnt = [0] * 30
5
6        # Count the number of 1 bits at each position
7        for num in nums:
8            for i in range(30):
9                if num & (1 << i):
10                    cnt[i] += 1
11
12        res = 0
13        for _ in range(k):
14            cur = 0
15            # Construct the current number from the most significant bit to the least significant bit
16            for j in range(29, -1, -1):
17                if cnt[j] > 0:
18                    cur |= 1 << j
19                    cnt[j] -= 1
20            res = (res + cur * cur) % MOD
21
22        return res