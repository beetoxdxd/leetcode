# Last updated: 1/8/2026, 5:25:41 p.m.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1

        while left < right:
            half = (left + right) // 2

            if arr[half] > arr[half+1]: right = half
            else: left = half+1

        return left
