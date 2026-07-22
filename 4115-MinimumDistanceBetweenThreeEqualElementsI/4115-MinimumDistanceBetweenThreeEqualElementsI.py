# Last updated: 22/7/2026, 5:56:18 p.m.
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        h = defaultdict(list)

        for i, num in enumerate(nums):
            h[num].append(i)

        ans = math.inf
        for k, tup in h.items():
            n = len(tup)
            if n < 3: continue

            for i in range(n-2):
                ans = min(ans, abs(tup[i] - tup[i+1]) + abs(tup[i+1] - tup[i+2]) + abs(tup[i+2] - tup[i]))

        if ans == math.inf: return -1
        return ans