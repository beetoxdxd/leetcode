# Last updated: 1/8/2026, 5:27:02 p.m.
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        vowels = "aeiouAEIOU"
        reversed = list(s)
        
        while i <= j:
            if not s[i] in vowels:
                i += 1
                continue
            if not s[j] in vowels:
                j -= 1
                continue

            aux = reversed[i]
            reversed[i] = reversed[j]
            reversed[j] = aux
            i += 1
            j -= 1

        return "".join(reversed)