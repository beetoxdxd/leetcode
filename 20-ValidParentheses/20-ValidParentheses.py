# Last updated: 1/8/2026, 5:29:11 p.m.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        for char in s:
            if char in opening: stack.append(char)
            elif not stack: return False
            elif opening.index(stack.pop()) != closing.index(char): return False

        return False if stack else True