# Last updated: 1/8/2026, 5:26:55 p.m.
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []

        def construction(number, n, i) -> None:
            hour, minute = (number & 960) >> 6, number & 63
            if hour > 11 or minute > 59: return

            if n == 0: 
                m = '0'+str(minute) if minute < 10 else str(minute)
                ans.append(str(hour)+':'+m)
                return

            while i < 10:
                construction(number | (1 << i), n-1, i+1)
                i += 1

        construction(0, turnedOn, 0)
        return ans