# Last updated: 1/8/2026, 5:23:51 p.m.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        h = set()
        cont = 0

        for i in range(len(s)-k+1):
            string = s[i:i+k]
            if string not in h:
                h.add(string)
                cont += 1

        return True if cont == 2**k else False