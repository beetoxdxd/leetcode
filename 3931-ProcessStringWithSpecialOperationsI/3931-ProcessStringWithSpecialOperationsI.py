# Last updated: 22/7/2026, 5:56:46 p.m.
class Solution:
    def processStr(self, s: str) -> str:
        ans = []

        for char in s:
            if char == '*': 
                if ans: ans.pop()
            elif char == '#':
                ans.extend(ans)
            elif char == '%':
                ans = ans[::-1]
            else:
                ans.append(char)


        return ''.join(ans)
