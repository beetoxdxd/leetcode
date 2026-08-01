# Last updated: 1/8/2026, 5:27:14 p.m.
class MyQueue:

    def __init__(self):
        self.stack = []
        self.aux = []
        self.n = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.n += 1

    def pop(self) -> int:
        while self.stack:
            self.aux.append(self.stack.pop())
        elem = self.aux.pop()
        self.n -= 1

        while self.aux:
            self.stack.append(self.aux.pop())

        return elem

    def peek(self) -> int:
        while self.stack:
            self.aux.append(self.stack.pop())
        elem = self.aux[self.n]

        while self.aux:
            self.stack.append(self.aux.pop())
            
        return elem

    def empty(self) -> bool:
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()