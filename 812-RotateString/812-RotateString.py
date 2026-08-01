# Last updated: 1/8/2026, 5:25:53 p.m.
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m: return False

        index = []
        for i, char in enumerate(s):
            if char == goal[0]: index.append(i)

        for k in index:
            i = k
            equal = True
            for j in range(m):
                if s[i] != goal[j]: equal = False; break
                i = (i+1) % n

            if equal: return True

        return False