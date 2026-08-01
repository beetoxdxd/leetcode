# Last updated: 1/8/2026, 5:25:30 p.m.
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        distinct = set()
        prev = set()

        for i in range(n):
            current = {arr[i] | p for p in prev}
            current.add(arr[i])
            distinct.update(current)
            prev = current

        return len(distinct)