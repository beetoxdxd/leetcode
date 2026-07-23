# Last updated: 22/7/2026, 11:35:36 p.m.
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        direction = 0
        blanks = 0

        for mov in moves:
            if mov == 'L': direction -= 1
            elif mov == 'R': direction += 1
            else: blanks += 1

        return abs(direction) + blanks