# Last updated: 27/8/2026, 4:59:17 p.m.
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        i = n//2 - 1
        j = n-1
        stop = i+1 if n % 2 == 0 else i+2
        cont = 0

        while i >= 0 and j >= stop:
            if nums[i] < nums[j]:
                i -= 1
                j -= 1
                cont += 2
            else:
                i -= 1

        return n - cont