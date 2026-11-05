# Last updated: 4/11/2026, 10:49:00 p.m.
1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        arr2.sort()
4        n = len(arr2)
5        ans = 0
6
7        for num in arr1:
8            i = bisect.bisect_right(arr2, num)
9            if i > 0 and num - arr2[i-1] <= d: continue
10            if i < n and arr2[i] - num <= d: continue
11
12            ans += 1
13
14        return ans