# Last updated: 22/7/2026, 11:35:12 p.m.
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pq = [(wt, wt, 1) for i, wt in enumerate(workerTimes)]
        heapq.heapify(pq)
        ans = 0

        for i in range(mountainHeight):
            seconds, workerTime, mult = heapq.heappop(pq)
            ans = max(seconds, ans)
            heapq.heappush(pq, (seconds + workerTime*(mult+1), workerTime, mult+1))

        return ans