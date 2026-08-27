# Last updated: 27/8/2026, 4:58:57 p.m.
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        j = 0
        h = {}
        ans = 0
        nums = [ord(char) - ord('0') for char in s]

        for i, num in enumerate(nums):
            if num not in h: h[num] = 2

            ans = max(ans, i-j)
            while j < i and h[num] == 0:
                h[nums[j]] += 1
                j += 1

            h[num] -= 1

        return max(ans, i+1-j)