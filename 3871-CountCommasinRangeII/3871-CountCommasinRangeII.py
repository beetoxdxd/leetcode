# Last updated: 9/9/2026, 1:53:36 a.m.
1class Solution:
2    def countCommas(self, n: int) -> int:
3        prefix = [10** i for i in range(0, 16, 3)]
4        for i in range(1, len(prefix)):
5            prefix[i] = prefix[i] + prefix[i-1] - 1
6
7        aux = n
8        mult = 0
9        while aux >= 1000: 
10            aux //= 1000
11            mult += 1
12
13        return mult*n - prefix[mult] + 1