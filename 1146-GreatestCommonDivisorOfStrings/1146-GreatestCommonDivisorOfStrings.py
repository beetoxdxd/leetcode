# Last updated: 1/8/2026, 5:25:04 p.m.
class Solution:
    def min_max(self, str1: str, str2: str) -> tuple:
        len1 = len(str1)
        len2 = len(str2)
        if len1 < len2:
            return (len1, len2, str1, str2)
        return (len2, len1, str2, str1)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_min, len_max, str_min, str_max = self.min_max(str1, str2)
        i = 2
        longest = ""

        while i <= len_min:
            if len_min % i != 0 or len_max % i != 0:
                i += 1
                continue

            aux = 0
            inc = i
            print(str_min[:inc])
            while inc <= len_min and str_min[aux:inc] == str_max[aux:inc]:
                aux = inc
                inc += i
            
            if inc <= len_min:
                i += 1
                continue
            
            while inc <= len_max and str_max[aux:inc] == str_max[:i]:
                aux = inc
                inc += i
            
            i += 1
            if inc <= len_max:
                continue
            else:
                longest = str_min[:i-1]

        if i == 2 and str_min[0] == str_max[0]:
            return str_min[0]

        return longest

