# Last updated: 12/10/2026, 10:50:40 p.m.
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            nums[i] **= 2
5
6        queue = deque(sorted(nums))
7        ans = 0
8        
9        while queue:
10            ans += queue.pop()
11            if queue: ans -= queue.popleft()
12
13        return ans