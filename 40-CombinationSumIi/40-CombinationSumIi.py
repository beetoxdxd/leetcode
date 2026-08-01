# Last updated: 1/8/2026, 5:28:35 p.m.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def traverse(acc: int, comb: List[int], j: int) -> None:
            if acc == target:
                ans.append(list(comb)) 
                return
            
            for i in range(j, len(candidates)):
                current_sum = acc + candidates[i]
                if current_sum > target:
                    break
                
                if i > j and candidates[i] == candidates[i-1]:
                    continue
                
                comb.append(candidates[i])
                traverse(current_sum, comb, i + 1)
                comb.pop()

        traverse(0, [], 0)
        return ans