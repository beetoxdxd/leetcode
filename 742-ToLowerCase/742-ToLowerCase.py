# Last updated: 1/8/2026, 5:26:08 p.m.
class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in s)