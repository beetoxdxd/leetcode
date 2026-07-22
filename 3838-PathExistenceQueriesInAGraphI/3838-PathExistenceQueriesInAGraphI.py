# Last updated: 22/7/2026, 5:56:58 p.m.
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        nodes = [0] * n
        current_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            nodes[i] = current_id

        return [nodes[u] == nodes[v] for u, v in queries]