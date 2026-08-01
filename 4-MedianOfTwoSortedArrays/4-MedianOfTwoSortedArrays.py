# Last updated: 1/8/2026, 5:29:40 p.m.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        aux = nums1 + nums2
        aux.sort()
        size = len(aux)
        if size%2 != 0: return aux[size//2]
        return (aux[size//2] + aux[size//2 - 1]) / 2
'''
        while low <= high:
            half = (low + high) // 2
            if num < nums1[half]:
                high = half - 1
            elif num > nums1[half]:
                low = half + 1
            elif num == nums1[half]: return True

        [1,2,3,4]

        '''