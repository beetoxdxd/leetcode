# Last updated: 1/8/2026, 5:25:05 p.m.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        size = -1

        for char in s:
            if stack and char == stack[size]:
                while stack and char == stack[size]:
                    stack.pop()
                    size -= 1   
            else:
                stack.append(char)
                size += 1 
        
        return ''.join(stack)