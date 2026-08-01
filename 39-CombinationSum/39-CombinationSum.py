# Last updated: 1/8/2026, 5:28:38 p.m.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def traverse(acc: int, comb: List[int], j: int) -> None:
            for i in range(j, len(candidates)):
                current_sum = acc + candidates[i]
                if current_sum >= target:
                    if current_sum == target: ans.append(comb + [candidates[i]])
                    return
                else:
                    traverse(current_sum, comb + [candidates[i]], i)

        traverse(0, [], 0)
        return ans