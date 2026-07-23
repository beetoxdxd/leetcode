# Last updated: 22/7/2026, 11:35:06 p.m.
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        next = [[0] * 26 for _ in range(26)]
        prev = [[0] * 26 for _ in range(26)]

        for i in range(26):
            j = (i+1) % 26
            k = (i-1) % 26

            while j != i:
                next[i][j] = next[i][j-1] + nextCost[j-1]
                if k == 25: prev[i][k] = prev[i][0] + previousCost[0]
                else: prev[i][k] = prev[i][k+1] + previousCost[k+1]
                k = (k-1) % 26
                j = (j+1) % 26

        ans = 0
        for l, r in zip(s, t):
            i, j = ord(l) - ord('a'), ord(r) - ord('a')
            ans += min(next[i][j], prev[i][j])
        return ans