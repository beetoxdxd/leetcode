# Last updated: 1/8/2026, 5:28:27 p.m.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def traverse(perm: List[int], used: List[int]) -> None:
            if len(perm) == n: 
                if perm not in ans: ans.append(perm)
                return 

            for i in range(n):
                if i not in used: 
                    traverse(perm + [nums[i]], used + [i]) 

        traverse([], [])
        return ans