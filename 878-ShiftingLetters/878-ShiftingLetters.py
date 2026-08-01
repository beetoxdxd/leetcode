# Last updated: 1/8/2026, 5:25:43 p.m.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        acc = 0
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = ""

        for i in range(len(shifts)-1, -1, -1):
            acc += shifts[i] % 26
            shifts[i] = acc 

        for i,char in enumerate(s):
            ans += abc[(ord(char) - ord('a') + shifts[i]) % 26]

        return ans