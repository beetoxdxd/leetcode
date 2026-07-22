# Last updated: 22/7/2026, 5:57:09 p.m.
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        word = [''] * (n+m-1)
        mov = [False] * (n+m-1)


        for i, char in enumerate(str1):
            if char == 'T':
                for j in range(i, m+i):
                    if word[j] != '' and word[j] != str2[j-i]: return ''
                    word[j] = str2[j-i]

        for i, char in enumerate(word):
            if char == '':
                word[i] = 'a'
                mov[i] = True

        for i, char in enumerate(str1):
            if char == 'F':
                if word[i:m+i] == list(str2):
                    not_possible = True

                    for j in range(m+i-1, i-1, -1):
                        if mov[j]: 
                            word[j] = 'b'
                            not_possible = False
                            break

                    if not_possible: return ''
                

        return ''.join(word)