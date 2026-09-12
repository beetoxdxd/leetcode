# Last updated: 12/9/2026, 3:47:02 p.m.
1class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        arr = [
5            (intervals[i][1], intervals[i][0], intervals[i][2], i)
6            for i in range(n)
7        ]
8        # Sort by right endpoint.
9        arr.sort(key=lambda x: x[0])
10
11        dp = [[0] * 5 for _ in range(n + 1)]
12        indices = [[[] for _ in range(5)] for _ in range(n + 1)]
13
14        for i in range(n):
15            r, l, weight, idx = arr[i]
16            # Use binary search to find intervals whose right endpoints are smaller than l.
17            k = bisect_left(arr, (l,), hi=i)
18
19            for j in range(1, 5):
20                s1 = dp[i][j]
21                s2 = dp[k][j - 1] + weight
22                if s1 > s2:
23                    dp[i + 1][j] = dp[i][j]
24                    indices[i + 1][j] = indices[i][j].copy()
25                    continue
26
27                new_index = indices[k][j - 1].copy()
28                new_index.append(idx)
29                new_index.sort()
30                if s1 == s2 and indices[i][j] < new_index:
31                    new_index = indices[i][j].copy()
32                dp[i + 1][j] = s2
33                indices[i + 1][j] = new_index
34
35        return indices[n][4]