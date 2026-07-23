# Last updated: 22/7/2026, 11:35:24 p.m.
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        n = len(capacity)
        i = 0
        apples = sum(apple)

        while i < n and apples > 0:
            apples -= capacity[i]
            i += 1

        return i