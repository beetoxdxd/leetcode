# Last updated: 1/8/2026, 5:29:36 p.m.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [[] for _ in range(numRows)]
        sense = False # False = down, True = up
        i = 0

        for char in s:
            if i == 0: sense = False
            elif i == numRows-1: sense = True
            rows[i].append(char)

            if sense: i -= 1
            else: i += 1

        ans = ''
        for row in rows:
            ans += ''.join(row)

        return ans