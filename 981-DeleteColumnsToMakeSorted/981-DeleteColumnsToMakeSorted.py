# Last updated: 1/8/2026, 5:25:23 p.m.
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        ans = 0

        for i in range(len(strs[0])):
            flag = True
            for j in range(1, n):
                if strs[j][i] < strs[j-1][i]:
                    flag = False
                    break
            
            if flag is False:
                ans += 1

        return ans
