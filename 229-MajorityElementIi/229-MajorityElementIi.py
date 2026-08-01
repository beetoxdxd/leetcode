# Last updated: 1/8/2026, 5:27:17 p.m.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n//3
        occurrences = defaultdict(int)
        
        for num in nums:
            occurrences[num] += 1
            
        ans = []
        keys = list(occurrences.keys())
        for key in keys:
            if occurrences[key] > limit: ans.append(key)
                
        return ans