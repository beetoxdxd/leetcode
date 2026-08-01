# Last updated: 1/8/2026, 5:23:22 p.m.
class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.history = []

    def append(self, val: int) -> None:
        normalized_val = (val - self.add) * pow(self.mul, -1, self.MOD) % self.MOD
        self.history.append(normalized_val)

    def addAll(self, inc: int) -> None:
        self.add += inc % self.MOD

    def multAll(self, m: int) -> None:
        self.mul *= m % self.MOD
        self.add *= m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.history): return -1
        return (self.history[idx] * self.mul + self.add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)