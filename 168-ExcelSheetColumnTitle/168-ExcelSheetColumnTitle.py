# Last updated: 1/8/2026, 5:27:33 p.m.
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        
        while columnNumber > 0:
            columnNumber -= 1
            div = columnNumber % 26
            ans += h[div]
            columnNumber //= 26

        return ans[::-1]
