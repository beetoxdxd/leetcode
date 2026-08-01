# Last updated: 1/8/2026, 5:25:26 p.m.
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        n = len(arr)
        while i < n and arr[i-1] < arr[i]: i += 1
        if i == 1 or i == n: return False
        while i < n and arr[i-1] > arr[i]: i += 1

        return i == n