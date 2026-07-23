# Last updated: 22/7/2026, 11:36:18 p.m.
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(word.lower() if len(word) <= 2 else word.capitalize() for word in title.split(' '))