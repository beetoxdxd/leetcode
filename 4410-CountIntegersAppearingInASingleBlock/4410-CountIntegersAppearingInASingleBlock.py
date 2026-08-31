# Last updated: 30/8/2026, 11:31:54 p.m.
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        h = defaultdict(list)

        for i, num in enumerate(nums):
            h[num].append(i)

        ans = 0
        for num, indices in h.items():
            expected = indices[0] + 1
            flag = False

            for i in range(1, len(indices)):
                if indices[i] != expected:
                    flag = True
                    break

                expected += 1

            if not flag: ans += 1

        return ans