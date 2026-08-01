# Last updated: 1/8/2026, 5:23:49 p.m.
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        row = [-math.inf] * (len(nums1)+1)

        for i in range(len(nums2)):
            prev_diagonal = -math.inf
            for j in range(len(nums1)):
                aux = nums1[j] * nums2[i]
                upper = row[j+1]
                row[j+1] = max(aux, upper, row[j], aux + prev_diagonal)
                prev_diagonal = upper

        return row[-1]