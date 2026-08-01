# Last updated: 1/8/2026, 5:28:17 p.m.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        n = len(nums)
        queue = deque([0])

        while queue:
            current = queue.popleft()
            if far >= n-1: return True
            #print(current)

            for i in range(max(far, current), min(n, current + nums[current])):
                queue.append(i+1)
            #print(queue)

            far = max(far, current + nums[current])

        return False