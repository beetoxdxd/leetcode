# Last updated: 1/8/2026, 5:22:14 p.m.
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 if pat in word else 0 for pat in patterns)