# Last updated: 10/10/2026, 1:23:41 p.m.
1class Solution:
2    def minSumSquareDiff(
3        self, nums1: List[int], nums2: List[int], k1: int, k2: int
4    ) -> int:
5        k = k1 + k2
6        d = [abs(a - b) for a, b in zip(nums1, nums2)]
7        if sum(d) <= k:
8            return 0
9
10        d.sort(reverse=True)
11        d.append(0)
12        n = len(nums1)
13
14        for i in range(1, n + 1):
15            cost = (d[i - 1] - d[i]) * i
16            if cost > k:
17                q, r = divmod(k, i)
18                hi = d[i - 1] - q
19                return (
20                    hi * hi * (i - r)
21                    + (hi - 1) * (hi - 1) * r
22                    + sum(x * x for x in d[i:n])
23                )
24            k -= cost
25        return 0