# Last updated: 1/8/2026, 5:22:31 p.m.
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 1

        while i < n and j < m:
            if nums1[i] > nums2[j]: i += 1
            j += 1

        return j-i-1