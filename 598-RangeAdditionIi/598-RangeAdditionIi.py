# Last updated: 1/8/2026, 5:26:35 p.m.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n

        m = min(op[0] for op in ops)
        n = min(op[1] for op in ops)
        return m*n