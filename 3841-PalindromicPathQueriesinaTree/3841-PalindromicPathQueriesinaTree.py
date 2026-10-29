# Last updated: 28/10/2026, 9:35:15 p.m.
1class BIT:
2    def __init__(self, n: int):
3        self.n = n
4        self.tree = [0] * (n + 1)
5
6    @staticmethod
7    def lowbit(x: int) -> int:
8        return x & -x
9
10    def update(self, x: int, v: int) -> None:
11        while x <= self.n:
12            self.tree[x] ^= v
13            x += BIT.lowbit(x)
14
15    def query(self, x: int) -> int:
16        ret = 0
17        while x:
18            ret ^= self.tree[x]
19            x -= BIT.lowbit(x)
20        return ret
21
22    def updateRange(self, l: int, r: int, v: int) -> None:
23        self.update(l, v)
24        self.update(r + 1, v)
25
26
27class Solution:
28    def palindromePath(
29        self, n: int, edges: List[List[int]], s: str, queries: List[str]
30    ) -> List[bool]:
31        g = [[] for _ in range(n)]
32        for u, v in edges:
33            g[u].append(v)
34            g[v].append(u)
35
36        LOG = n.bit_length()
37        fa = [[0] * LOG for _ in range(n)]
38        dep = [0] * n
39        l = [0] * n
40        r = [0] * n
41        timer = 0
42
43        def dfs(u: int, p: int) -> None:
44            nonlocal timer
45            timer += 1
46            l[u] = timer
47            fa[u][0] = p
48            for v in g[u]:
49                if v == p:
50                    continue
51                dep[v] = dep[u] + 1
52                dfs(v, u)
53            r[u] = timer
54
55        dfs(0, 0)
56
57        for j in range(1, LOG):
58            for i in range(n):
59                fa[i][j] = fa[fa[i][j - 1]][j - 1]
60
61        def lca(u: int, v: int) -> int:
62            if dep[u] < dep[v]:
63                u, v = v, u
64            diff = dep[u] - dep[v]
65            for i in range(LOG):
66                if (diff >> i) & 1:
67                    u = fa[u][i]
68            if u == v:
69                return u
70            for i in range(LOG - 1, -1, -1):
71                if fa[u][i] != fa[v][i]:
72                    u = fa[u][i]
73                    v = fa[v][i]
74            return fa[u][0]
75
76        bit = BIT(n + 1)
77        s = list(s)
78        for i in range(n):
79            bit.updateRange(l[i], r[i], 1 << (ord(s[i]) - ord("a")))
80
81        ans = []
82        for q in queries:
83            op, *rest = q.split()
84            if op == "update":
85                u, c = int(rest[0]), rest[1]
86                bit.updateRange(
87                    l[u],
88                    r[u],
89                    (1 << (ord(s[u]) - ord("a"))) ^ (1 << (ord(c) - ord("a"))),
90                )
91                s[u] = c
92            else:
93                u, v = int(rest[0]), int(rest[1])
94                w = lca(u, v)
95                mask = (
96                    bit.query(l[u])
97                    ^ bit.query(l[v])
98                    ^ (1 << (ord(s[w]) - ord("a")))
99                )
100                ans.append(mask.bit_count() <= 1)
101        return ans