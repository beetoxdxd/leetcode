# Last updated: 1/8/2026, 5:22:37 p.m.
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        prev_id, prev_h = 1, 0

        for i in range(1, len(restrictions)):
            curr_id, curr_h = restrictions[i]

            distance = curr_id - prev_id
            height = distance + prev_h

            prev_id = curr_id
            prev_h = min(curr_h, height)
            restrictions[i][1] = prev_h

        prev_id, prev_h = restrictions[-1]
        for i in range(len(restrictions)-2, -1, -1):
            curr_id, curr_h = restrictions[i]

            distance = prev_id - curr_id
            height = distance + prev_h

            prev_id = curr_id
            prev_h = min(curr_h, height)
            restrictions[i][1] = prev_h

        ans = 0
        for i in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[i-1]
            curr_id, curr_h = restrictions[i]

            ans = max(ans, (prev_h + curr_h + curr_id - prev_id)//2)

        return max(ans, restrictions[-1][1] + n - restrictions[-1][0])