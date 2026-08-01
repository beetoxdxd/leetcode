# Last updated: 1/8/2026, 5:22:02 p.m.
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        string = str(n)
        values = [0]*10

        while True:
            for i in range(len(string)):
                values[ord(string[i]) - ord('0')] += 1

            i = 1
            if values[0] == 0:
                while i < 10:
                    if values[i] != 0 and values[i] != i: break
                    i += 1
                if i == 10: return int(string)
                
            values = [0]*10
            string = str(int(string) + 1)