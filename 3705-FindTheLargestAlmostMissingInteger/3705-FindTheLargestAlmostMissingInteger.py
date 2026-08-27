# Last updated: 27/8/2026, 4:58:00 p.m.
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n: return max(nums)

        cont = defaultdict(int)
        for num in nums:
            cont[num] += 1

        if k == 1:
            ans = -1
            for key, value in cont.items():
                if value == 1: ans = max(ans, key)

            return ans

        left = cont[nums[0]] > 1
        right = cont[nums[-1]] > 1

        if left and right: return -1
        if left: return nums[-1]
        if right: return nums[0]

        return max(nums[0], nums[-1])