# Last updated: 1/8/2026, 5:26:24 p.m.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0

        for move in moves:
            if move == 'U': vertical += 1
            elif move == 'D': vertical -= 1
            elif move == 'R': horizontal += 1
            else: horizontal -= 1

        return vertical == 0 and horizontal == 0