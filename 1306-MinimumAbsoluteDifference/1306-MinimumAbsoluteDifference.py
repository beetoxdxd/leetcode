# Last updated: 1/8/2026, 5:24:40 p.m.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = [[0, math.inf]]

        for i in range(1,len(arr)):
            sub = abs(arr[i] - arr[i-1])
            min_sub = abs(ans[0][1] - ans[0][0])

            if sub <= min_sub: 
                if sub < min_sub: ans.clear()
                ans.append([arr[i-1], arr[i]])

        return ans