# Last updated: 1/8/2026, 5:24:29 p.m.
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        one = []
        set1 = {''}
        set2 = {''}

        for i in nums1:
            set1.add(i)
        for i in nums2:
            set2.add(i)

        print(set1, set2)
        for i in set1:
            if not i in set2: one.append(i)
        answer.append(one[:])
        one.clear()
        for i in set2:
            if not i in set1: one.append(i)

        answer.append(one)
        return answer