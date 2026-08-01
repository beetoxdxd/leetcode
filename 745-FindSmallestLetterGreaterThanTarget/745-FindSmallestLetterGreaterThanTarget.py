# Last updated: 1/8/2026, 5:26:06 p.m.
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i, j = 0, len(letters)-1
        ans = letters[0]

        while i <= j:
            h = (i+j)//2
            if letters[h] > target: #try with previous value
                ans = letters[h]
                j = h-1
            else: i = h+1
            
        return ans