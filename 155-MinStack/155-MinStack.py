# Last updated: 1/8/2026, 5:27:35 p.m.
class MinStack:

    def __init__(self):
        self.t = 0
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.insert(self.t, val)
        self.t += 1
        if not self.min: self.min.append(val)
        elif self.min[0] >= val: self.min.insert(0, val)

    def pop(self) -> None:
        if self.stack[self.t-1] == self.min[0]: self.min.pop(0)
        self.stack.pop()
        self.t -= 1

    def top(self) -> int:
        return self.stack[self.t-1]

    def getMin(self) -> int:
        return self.min[0]