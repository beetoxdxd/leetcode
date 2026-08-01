# Last updated: 1/8/2026, 5:27:39 p.m.
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] != "":
                reversed += words[i] + " "

        return reversed[:-1]

