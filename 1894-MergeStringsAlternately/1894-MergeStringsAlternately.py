# Last updated: 1/8/2026, 5:22:44 p.m.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        i = 0
        word1_size = len(word1)
        word2_size = len(word2)

        while i < word1_size and i < word2_size:
            merge += word1[i] + word2[i]
            i += 1
        
        if i < word1_size:
            merge += word1[i:]
        else:
            merge += word2[i:]

        return merge