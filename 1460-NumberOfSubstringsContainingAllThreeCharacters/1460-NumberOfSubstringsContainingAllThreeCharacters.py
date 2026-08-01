# Last updated: 1/8/2026, 5:24:12 p.m.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        abc = deque()
        h = [0]*3
        ans = 0

        for i, char in enumerate(s):
            abc.append(char)
            h[ord(char) - 97] += 1

            while h[0] > 0 and h[1] > 0 and h[2] > 0:
                h[ord(abc.popleft()) - 97] -= 1
                ans += n - i

        return ans