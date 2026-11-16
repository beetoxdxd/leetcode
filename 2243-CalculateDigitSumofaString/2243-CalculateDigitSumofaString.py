# Last updated: 15/11/2026, 11:42:50 p.m.
1class Solution:
2    def digitSum(self, s: str, k: int) -> str:
3        
4        while len(s) > k:
5            print(s)
6            aux = ''
7            num = 0
8
9            for i in range(len(s)):
10                num += int(s[i])
11
12                if (i+1) % k == 0:
13                    aux += str(num)
14                    num = 0
15            
16            if len(s) % k: aux += str(num)
17            s = aux
18
19        return s