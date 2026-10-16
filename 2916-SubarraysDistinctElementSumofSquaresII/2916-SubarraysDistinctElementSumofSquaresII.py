# Last updated: 15/10/2026, 9:27:23 p.m.
1class BIT:
2    def __init__(self, n: int):
3        self.size = n
4        self._tree1 = defaultdict(int)
5        self._tree2 = defaultdict(int)
6
7    def _lowbit(self, index: int) -> int:
8        return index & -index
9
10    def add(self, left: int, right: int, delta: int) -> None:
11        self._add(left, delta)
12        self._add(right + 1, -delta)
13
14    def query(self, left: int, right: int) -> int:
15        return self._query(right) - self._query(left - 1)
16
17    def _add(self, index: int, delta: int) -> None:
18        index += 1
19        rawIndex = index
20        while index <= self.size:
21            self._tree1[index] += delta
22            self._tree2[index] += (rawIndex - 1) * delta
23            index += self._lowbit(index)
24
25    def _query(self, index: int) -> int:
26        index += 1
27        if index > self.size:
28            index = self.size
29
30        rawIndex = index
31        res = 0
32        while index > 0:
33            res += rawIndex * self._tree1[index] - self._tree2[index]
34            index -= self._lowbit(index)
35        return res
36
37
38class Solution:
39    def sumCounts(self, A: List[int]) -> int:
40        n = len(A)
41        res = cur = 0
42        bit = BIT(n + 10)
43        seen = {}
44        mod = 10**9 + 7
45        for i, a in enumerate(A):
46            j = seen.get(a, -1) + 1
47            cur = (cur + bit.query(j, i) * 2 + i - j + 1) % mod
48            res = (res + cur) % mod
49            bit.add(j, i, 1)
50            seen[a] = i
51        return res