# Last updated: 1/8/2026, 5:23:17 p.m.
class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = s.count('a')
        count_b = 0
        ans = count_a + count_b

        for char in s:
            if char == 'a': count_a -= 1
            else: count_b += 1

            ans = min(count_a + count_b, ans)

        return ans