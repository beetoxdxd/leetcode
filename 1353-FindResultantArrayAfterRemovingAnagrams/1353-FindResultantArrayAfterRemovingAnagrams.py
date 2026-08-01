# Last updated: 1/8/2026, 5:24:35 p.m.
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        h = []
        for i in range(len(words)):
            aux = [0] * 26
            for char in words[i]: aux[ord(char) - ord('a')] += 1
            h.append(aux)

        
        for i in range(len(words)-1, 0, -1):
            if h[i] == h[i-1]: words.pop(i)

        return words