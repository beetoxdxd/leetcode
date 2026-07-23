# Last updated: 22/7/2026, 11:35:29 p.m.
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h = sorted(hFences + [1,m])
        v = sorted(vFences + [1,n])
        
        k = len(h)
        diff_h = {h[j] - h[i] for i in range(k-1) for j in range(i+1, k)}

        k = len(v)
        max_side = -1
        for i in range(k-1):
            for j in range(i+1, k):
                gap = v[j] - v[i]
                if gap in diff_h and gap > max_side: max_side = gap

        return max_side**2 % (10**9 + 7) if max_side != -1 else -1
