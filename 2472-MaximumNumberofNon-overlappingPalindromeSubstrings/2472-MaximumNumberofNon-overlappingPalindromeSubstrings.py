# Last updated: 14/9/2026, 10:09:50 p.m.
1class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        def palindrome(i: int, j: int) -> bool:
4            while i < j:
5                if s[i] != s[j]: break
6                i += 1
7                j -= 1
8
9            return i >= j
10            
11        n = len(s)
12        i = 0
13        ans = 0
14
15        while i < n:
16            if k+i-1 < n and palindrome(i, k+i-1):
17                i += k; ans += 1
18            elif k+i < n and palindrome(i, k+i):
19                i += k+1; ans += 1
20            else:
21                i += 1
22
23        return ans