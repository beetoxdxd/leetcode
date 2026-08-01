# Last updated: 1/8/2026, 5:22:26 p.m.
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue = deque([0])

        far = 0
        while queue:
            current = queue.popleft()
            if current == n-1: return True

            for i in range(max(current+minJump, far+1), min(current+maxJump+1, n)):
                if s[i] == '0': queue.append(i)
            
                far = max(far, i)

        return False