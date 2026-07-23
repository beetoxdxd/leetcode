# Last updated: 22/7/2026, 11:35:38 p.m.
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0]*26
        odds = [0]*26

        for i in range(len(s1)):
            index1 = ord(s1[i]) - 97 # ord('a')
            index2 = ord(s2[i]) - 97
            
            if i % 2:
                even[index1] += 1
                even[index2] -= 1
            else:
                odds[index1] += 1
                odds[index2] -= 1

        for i in range(26):
            if even[i] != 0 or odds[i] != 0: return False

        return True