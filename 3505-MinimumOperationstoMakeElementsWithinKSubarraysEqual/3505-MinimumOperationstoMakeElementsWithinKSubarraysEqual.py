# Last updated: 3/11/2026, 11:21:49 p.m.
1class Window:
2    """A sorted window that keeps the sum of its h = x // 2 smallest values."""
3
4    def __init__(self, values):
5        self.h, self.odd = len(values) // 2, len(values) & 1
6        self.sorted = SortedList(values)
7        self.low, self.total = sum(self.sorted[:self.h]), sum(values)
8
9    @property
10    def cost(self):  # larger half minus smaller half
11        return self.total - 2 * self.low - self.odd * self.sorted[self.h]
12
13    def slide(self, out, new):
14        s, h = self.sorted, self.h
15        if new < s[h - 1]:  # new joins the h smallest and pushes their largest up
16            self.low += new - s[h - 1]
17        s.add(new)
18        if out <= s[h - 1]:  # out was among the h smallest: the next value moves down
19            self.low += s[h] - out
20        s.remove(out)
21        self.total += new - out
22        return self.cost
23
24
25class Solution:
26    def minOperations(self, nums: List[int], x: int, k: int) -> int:
27        win = Window(nums[:x])
28        cost = [win.cost] + [win.slide(out, new) for out, new in zip(nums, nums[x:])]
29        best = [0] * (len(nums) + 1)  # best[i]: min ops for the windows placed so far inside nums[:i]
30        for _ in range(k):
31            best = list(accumulate([inf] * x + [b + c for b, c in zip(best, cost)], min))
32        return best[-1]