# Last updated: 22/7/2026, 11:35:11 p.m.
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) % 2 else "Bob"