# Last updated: 22/7/2026, 5:56:10 p.m.
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_elem = 0
        prefixGcd = []

        for num in nums:
            if num > max_elem: max_elem = num
            prefixGcd.append(math.gcd(num, max_elem))

        prefixGcd.sort()
        i, j = 0, len(prefixGcd)-1
        ans = 0

        while i < j:
            ans += math.gcd(prefixGcd[i], prefixGcd[j])
            i, j = i+1, j-1

        return ans