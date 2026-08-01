# Last updated: 1/8/2026, 5:27:42 p.m.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                x = stack.pop()
                stack.append(stack.pop() - x)
            elif token == '/':
                x = stack.pop()
                stack.append(int(float(stack.pop()) / x))
            else:
                stack.append(int(token))

        return stack.pop()