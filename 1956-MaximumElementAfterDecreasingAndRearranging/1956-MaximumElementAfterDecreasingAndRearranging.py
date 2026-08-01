# Last updated: 1/8/2026, 5:22:41 p.m.
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)

        return arr[-1]