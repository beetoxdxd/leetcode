# Last updated: 22/7/2026, 11:35:25 p.m.
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        h = set()
        for num in arr1:
            string = str(num)
            aux = ''
            for char in string:
                aux += char
                h.add(aux)

        ans = 0
        for num in arr2:
            string = str(num)
            aux = ''
            for char in string:
                aux += char
                if aux in h: 
                    ans = max(ans, len(aux))
                    h.remove(aux)

        return ans