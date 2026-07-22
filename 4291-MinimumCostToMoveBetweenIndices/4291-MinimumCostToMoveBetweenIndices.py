# Last updated: 22/7/2026, 5:56:09 p.m.
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        closest = [1]
        for i in range(1, n-1):
            if abs(nums[i] - nums[i-1]) <= abs(nums[i] - nums[i+1]): closest.append(i-1)
            else: closest.append(i+1)

        closest.append(n-2)

        cost_right = [0] * n
        cost_left = [0] * n
        j = n-2

        for i in range(1, n):
            if closest[i-1] == i: cost_right[i] = cost_right[i-1] + 1
            else: cost_right[i] = cost_right[i-1] + abs(nums[i] - nums[i-1])

            if closest[j+1] == j: cost_left[j] = cost_left[j+1] + 1
            else: cost_left[j] = cost_left[j+1] + abs(nums[j] - nums[j+1])

            j -= 1

        ans = []
        for start, end in queries:
            if end < start:
                ans.append(cost_left[end] - cost_left[start])
            else:
                ans.append(cost_right[end] - cost_right[start])

        return ans