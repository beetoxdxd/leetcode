# Last updated: 24/11/2026, 11:59:57 p.m.
1class Solution:
2    def smallestUniqueSubarray(self, nums):
3        MOD = 1000000007
4        BASE = 911382323
5
6        n = len(nums)
7        h = [0] * (n + 1)
8        p = [0] * (n + 1)
9        p[0] = 1
10
11        # Compute prefix hashes and powers of BASE
12        for i in range(n):
13            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
14            p[i + 1] = p[i] * BASE % MOD
15
16        def check(length):
17            cnt = {}
18            for l in range(n - length + 1):
19                r = l + length
20                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
21                cnt[key] = cnt.get(key, 0) + 1
22
23            for times in cnt.values():
24                if times == 1:
25                    return True
26            return False
27
28        lo, hi = 1, n
29        while lo < hi:
30            mid = lo + (hi - lo) // 2
31            if check(mid):
32                hi = mid
33            else:
34                lo = mid + 1
35
36        return lo