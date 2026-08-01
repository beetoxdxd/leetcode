# Last updated: 1/8/2026, 5:25:47 p.m.
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        ans = 0
        mod = 10**9 + 7 

        for i in range(len(arr)):
            ways = 1

            for j in range(i):
                if arr[j]**2 > arr[i]: break
                
                if arr[i] % arr[j] == 0:
                    div = arr[i] // arr[j]
                    if div in dp: # es divisor
                        if div == arr[j]: ways += dp[arr[j]] * dp[div]
                        else: ways += (dp[arr[j]] * dp[div])*2

            dp[arr[i]] = ways % mod
            ans = (ans + dp[arr[i]]) % mod

        return ans

