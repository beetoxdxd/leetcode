# Last updated: 12/10/2026, 10:51:31 p.m.
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            nums[i] **= 2
5
6        nums = deque(sorted(nums))
7        ans = 0
8        
9        while nums:
10            ans += nums.pop()
11            if nums: ans -= nums.popleft()
12
13        return ans