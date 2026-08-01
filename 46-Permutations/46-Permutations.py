# Last updated: 1/8/2026, 5:28:29 p.m.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def traverse(perm: List[int]) -> None:
            if len(perm) == n: 
                ans.append(perm)
                return 

            for num in nums:
                if num not in perm: 
                    traverse(perm + [num]) 

        traverse([])
        return ans