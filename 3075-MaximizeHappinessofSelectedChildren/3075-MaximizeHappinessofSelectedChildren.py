# Last updated: 26/10/2026, 12:26:47 a.m.
1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        pq = [-happy for happy in happiness]
4        heapq.heapify(pq)
5        ans, cont = 0, 0
6
7        while pq and k:
8            child = -heapq.heappop(pq)
9            if child - cont <= 0: break
10
11            ans += child - cont
12
13            k -= 1
14            cont += 1
15
16        return ans