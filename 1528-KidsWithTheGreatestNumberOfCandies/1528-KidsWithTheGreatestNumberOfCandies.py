# Last updated: 1/8/2026, 5:23:55 p.m.
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for kid in candies:
            if kid + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
