# Last updated: 1/8/2026, 5:27:13 p.m.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1]*l

        i, j = 1, l-2
        pref = nums[0]
        suf = nums[l-1]
        while i < l:
            ans[i] *= pref
            pref *= nums[i]
            ans[j] *= suf
            suf *= nums[j]
            i += 1
            j -= 1

        return ans

        # primera pasada [1, 1*1, 1*2, 1*2*3]
        # segunda pasada (al revés) [1*2*4, 1*2*3]
        # [2*3*4, 1*3*4, 1*2*4, 1*2*3]
