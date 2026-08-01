# Last updated: 1/8/2026, 5:29:28 p.m.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        prev_area = 0

        while i < j:
            area = (j-i)*min(height[i], height[j])
            if area > prev_area: 
                prev_area = area

            if height[j] > height[i]: i += 1
            else: j -= 1
    
        return prev_area