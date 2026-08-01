# Last updated: 1/8/2026, 5:24:09 p.m.
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        adj = []

        for i in range(n):
            indexes = []
            for j in range(1,d+1):
                if i + j < n and arr[i] > arr[i+j]: indexes.append(i+j)
                else: break

            for j in range(1, d+1):
                if i - j >= 0 and arr[i] > arr[i-j]: indexes.append(i-j)
                else: break

            adj.append(indexes)
        
        dp = [-1]*n
        def traverse(index: int) -> int:
            maximum = 0
            for i in adj[index]:
                if dp[i] != -1: reached = dp[i]
                else: reached = traverse(i)
                maximum = max(maximum, reached)
            
            dp[index] = 1 + maximum
            return dp[index]

        return max(traverse(i) for i in range(n))