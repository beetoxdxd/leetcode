# Last updated: 27/8/2026, 4:59:16 p.m.
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        number_ones = 0
        j = 0
        ans = math.inf

        for i, current in enumerate(s):
            if current == '1': number_ones += 1

            while number_ones > k: 
                if s[j] == '1': number_ones -= 1
                j += 1

            if number_ones == k:
                ans = min(ans, int(s[j:i+1], 2))

        return f"{ans:b}" if ans != math.inf else ''