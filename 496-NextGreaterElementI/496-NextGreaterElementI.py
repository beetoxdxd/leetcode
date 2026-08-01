# Last updated: 1/8/2026, 5:26:43 p.m.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums1:
            j = nums2.index(i)
            ind = -1
            for j in range(nums2.index(i), len(nums2)):
                if nums2[j] > i:
                    ind = nums2[j]
                    break
            ans.append(ind)
        return ans