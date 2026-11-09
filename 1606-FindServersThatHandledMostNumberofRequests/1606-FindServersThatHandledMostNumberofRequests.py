# Last updated: 9/11/2026, 12:08:23 a.m.
1class Solution:
2    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
3        free = list(range(k))  # already a heap: each free server is keyed by its next turn
4
5        handled, busy = [], []  # busy: (time it frees up, server)
6        for i, (t, d) in enumerate(zip(arrival, load)):
7            while busy and busy[0][0] <= t:  # done by time t
8                heappush(free, i + (heappop(busy)[1] - i) % k)  # its first turn from i on
9            if free:  # otherwise the request is dropped
10                x = heappop(free) % k
11                heappush(busy, (t + d, x))
12                handled.append(x)
13
14        return multimode(handled)