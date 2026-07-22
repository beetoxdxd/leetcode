# Last updated: 22/7/2026, 5:56:21 p.m.
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for num in range(num1, num2+1):
            string = str(num)
            for i in range(1, len(string)-1):
                if (string[i] > string [i-1] and string[i] > string[i+1]) or (string[i] < string [i-1] and string[i] < string[i+1]): ans += 1

        return ans