# Last updated: 1/8/2026, 5:26:12 p.m.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        size = -1
        i = 0
        length = len(asteroids)
        
        while i < length:
            elem = asteroids[i]
            if elem <= 0 and stack and stack[size] >= 0:
                if stack[size] > abs(elem): i += 1
                else:
                    if stack[size] == abs(elem): i += 1
                    stack.pop()
                    size -= 1
            else:
                stack.append(elem)
                size += 1
                i += 1
        return stack