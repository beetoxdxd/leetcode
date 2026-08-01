# Last updated: 1/8/2026, 5:29:42 p.m.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        m = 0
        cont = 0
        inicio = 0

        for i in range(len(s)):
            if s[i] in h:
                if m < cont: m = cont
                cont = i - h[s[i]] - 1
                for j in range(inicio, h[s[i]]):
                    del h[s[j]]
                    inicio += 1
                inicio += 1
                

            cont += 1
            h[s[i]] = i
        
        return m if m > cont else cont