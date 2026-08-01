# Last updated: 1/8/2026, 5:26:39 p.m.
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]) -> int:
            x1, y1 = p1
            x2, y2 = p2
            return (x2-x1)**2 + (y2-y1)**2

        glob = sorted([p1, p2, p3, p4])
        d1 = distance(glob[0], glob[2])
        d2 = distance(glob[2], glob[3])
        d3 = distance(glob[3], glob[1])
        d4 = distance(glob[1], glob[0])
        diag1, diag2 = distance(glob[0], glob[3]), distance(glob[2], glob[1])

        if d1 == d2 == d3 == d4 and diag1 == diag2 and d1+d2+d3+d4 != 0: return True
        return False
        # 0 -> 2 -> 3 -> 1 -> 0
        # A B C D