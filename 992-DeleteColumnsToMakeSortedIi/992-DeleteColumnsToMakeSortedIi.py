# Last updated: 1/8/2026, 5:25:21 p.m.
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deletions = 0
        
        is_sorted = [False] * (n - 1)

        for col in range(m):
            must_delete = False
            
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][col] > strs[i+1][col]:
                    must_delete = True
                    break
            
            if must_delete:
                deletions += 1
            else:
                for i in range(n - 1):
                    if strs[i][col] < strs[i+1][col]:
                        is_sorted[i] = True
                        
        return deletions