# Last updated: 1/8/2026, 5:23:04 p.m.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        op = 0

        for i in nums:
            if str(k-i) in dic:
                op += 1
                val = dic[str(k-i)] - 1
                if val <= 0: del dic[str(k-i)]
                else: dic[str(k-i)] = val
            else:
                if str(i) in dic: val = dic[str(i)]
                else: val = 0
                val += 1
                dic[str(i)] = val

        return op