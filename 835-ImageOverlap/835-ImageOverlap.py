# Last updated: 13/9/2026, 2:52:34 p.m.
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        ans = 0
5
6        dec1, dec2 = [0]*n, [0]*n
7        for i in range(n):
8            for j in range(n):
9                dec1[i] = (dec1[i] << 1) | img1[i][j]
10                dec2[i] = (dec2[i] << 1) | img2[i][j]
11
12        for up in range(n):
13            for right in range(n):
14                cont1, cont2, cont3, cont4 = 0, 0, 0, 0
15
16                for i in range(n-up):
17                    cont1 += (dec1[i] & (dec2[i+up] >> right)).bit_count()
18                    cont2 += ((dec1[i] >> right) & dec2[i+up]).bit_count()
19                    cont3 += (dec1[i+up] & (dec2[i] >> right)).bit_count()
20                    cont4 += ((dec1[i+up] >> right) & dec2[i]).bit_count()
21
22                ans = max(ans, cont1, cont2, cont3, cont4)
23
24        return ans