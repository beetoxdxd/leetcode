# Last updated: 17/10/2026, 11:56:31 p.m.
1class Solution:
2    def numOfWays(self, nums: List[int]) -> int:
3        mod = 10 ** 9 + 7
4        
5        def dfs(nums):
6            m = len(nums)
7            if m < 3: 
8                return 1
9            left_nodes = [a for a in nums if a < nums[0]]
10            right_nodes = [a for a in nums if a > nums[0]]
11            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
12        
13        return (dfs(nums) - 1) % mod