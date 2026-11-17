# Last updated: 16/11/2026, 10:40:20 p.m.
1class Solution:
2    def minimumChanges(self, s: str, k: int) -> int:
3        n = len(s)
4        divisors = [[] for _ in range(n + 1)]  # divisors[length]: every d < length that divides it
5        for d in range(1, n):
6            for length in range(2 * d, n + 1, d):
7                divisors[length].append(d)
8
9        @cache
10        def peel(i: int, j: int, d: int) -> int:  # s[i:j] in blocks of d: the outer pair of blocks, then the inside
11            if j - i <= d:
12                return 0  # no blocks or a single block: nothing to pair
13            return sum(map(ne, s[i:i + d], s[j - d:j])) + peel(i + d, j - d, d)
14
15        @cache
16        def cost(i: int, j: int) -> int:  # changes to make s[i:j] a semi-palindrome
17            return min(peel(i, j, d) for d in divisors[j - i])
18
19        best = {0: 0}  # best[j]: the fewest changes for s[:j] cut into the pieces placed so far
20        for pieces in range(1, k):  # every piece but the last
21            room = range(2 * pieces, n - 2 * (k - pieces) + 1)  # 2 letters for each piece, placed or still to come
22            best = {j: min(best[i] + cost(i, j) for i in best if i <= j - 2) for j in room}
23        return min(best[i] + cost(i, n) for i in best)  # the last piece ends at n