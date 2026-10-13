# Last updated: 12/10/2026, 10:53:15 p.m.
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        aux = SortedList()
4        for num in nums:
5            aux.add(num**2)
6
7        aux = deque(aux)
8        ans = 0
9        
10        while aux:
11            ans += aux.pop()
12            if aux: ans -= aux.popleft()
13
14        return ans