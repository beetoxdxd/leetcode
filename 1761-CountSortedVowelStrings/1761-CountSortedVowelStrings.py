# Last updated: 1/8/2026, 5:23:15 p.m.
class Solution:
    def countVowelStrings(self, n: int) -> int:
        abc = [1]*5
        number = 5

        for _ in range(n-1):
            prev = abc[0]
            abc[0] = number

            for i in range(1,5):
                number = abc[i]
                abc[i] = abc[i-1] - prev
                prev = number

            number = sum(abc)

        return number