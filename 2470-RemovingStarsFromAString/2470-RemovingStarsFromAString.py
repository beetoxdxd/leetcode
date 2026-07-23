# Last updated: 22/7/2026, 11:36:03 p.m.
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*": stack.pop()
            else: stack.append(char)
        return ''.join(stack)