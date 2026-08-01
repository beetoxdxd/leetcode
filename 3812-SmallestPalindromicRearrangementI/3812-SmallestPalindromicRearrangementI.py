# Last updated: 1/8/2026, 5:19:48 p.m.
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        h = [-1] * 26

        for char in s:
            h[ord(char) - 97] += 1

        odd = -1
        pal = []
        for i in range(26):
            if h[i] == -1: continue
            
            if h[i] % 2 == 0: odd = i
            times = (h[i] + 1) // 2
            pal.append(chr(i+97) * times)

        return ''.join(pal + pal[::-1]) if odd == -1 else ''.join(pal + [chr(odd + 97)] + pal[::-1])