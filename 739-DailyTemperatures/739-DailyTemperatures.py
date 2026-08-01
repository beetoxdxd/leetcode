# Last updated: 1/8/2026, 5:26:11 p.m.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        n = len(temperatures)
        ans = [0] * n

        for t in range(1, n):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = t-index

            stack.append(t)
        
        return ans