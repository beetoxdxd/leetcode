# Last updated: 1/8/2026, 5:25:14 p.m.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for point in points:
            x, y = point
            distance = sqrt(x**2 + y**2)
            distances.append((distance, point))
            
        distances.sort()
        ans = []
        for i in range(k):
            ans.append(distances[i][1])
        
        return ans