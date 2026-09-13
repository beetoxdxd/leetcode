# Last updated: 13/9/2026, 2:27:44 p.m.
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        ans = 0
5
6        for up in range(n):
7            for right in range(n):
8                cont1, cont2, cont3, cont4 = 0, 0, 0, 0
9
10                for i in range(n-up):
11                    for j in range(n-right):
12                        if img1[i][j] == 1 and img2[i+up][j+right] == 1: cont1 += 1
13                        if img1[i][j+right] == 1 and img2[i+up][j] == 1: cont2 += 1
14                        if img1[i+up][j] == 1 and img2[i][j+right] == 1: cont3 += 1
15                        if img1[i+up][j+right] == 1 and img2[i][j] == 1: cont4 += 1
16
17                ans = max(ans, cont1, cont2, cont3, cont4)
18
19        return ans