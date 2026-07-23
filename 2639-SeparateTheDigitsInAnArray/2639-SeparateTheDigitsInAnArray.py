# Last updated: 22/7/2026, 11:35:52 p.m.
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = [ord(item) - ord('0') for num in nums for item in str(num)]

        return ans