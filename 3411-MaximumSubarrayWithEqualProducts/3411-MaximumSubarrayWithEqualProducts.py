# Last updated: 23/11/2026, 11:05:02 p.m.
1class Solution:
2    def maxLength(self, nums: List[int]) -> int:
3        ans = 0
4        n = len(nums)
5
6        for i in range(n):
7            prod = lcm = gcd = nums[i]
8
9            for j in range(i+1, n):
10                prod *= nums[j]
11                lcm = math.lcm(lcm, nums[j])
12                gcd = math.gcd(gcd, nums[j])
13
14                if prod == lcm * gcd: 
15                    ans = max(ans, j-i+1)
16
17        return ans