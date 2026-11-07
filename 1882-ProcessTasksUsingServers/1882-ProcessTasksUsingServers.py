# Last updated: 7/11/2026, 4:37:00 p.m.
1class Solution:
2    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
3        # Busy servers, stored as pairs (t, idx)
4        busy = list()
5
6        # Idle servers, stored as pairs (w, idx)
7        idle = [(w, i) for i, w in enumerate(servers)]
8        heapq.heapify(idle)
9
10        ts = 0
11
12        # Move servers with t<=ts from priority queue busy to priority queue idle one by one
13        def release():
14            while busy and busy[0][0] <= ts:
15                _, idx = heapq.heappop(busy)
16                heapq.heappush(idle, (servers[idx], idx))
17
18        ans = list()
19        for i, task in enumerate(tasks):
20            ts = max(ts, i)
21            release()
22            if not idle:
23                ts = busy[0][0]
24                release()
25
26            _, idx = heapq.heappop(idle)
27            ans.append(idx)
28            heapq.heappush(busy, (ts + task, idx))
29
30        return ans