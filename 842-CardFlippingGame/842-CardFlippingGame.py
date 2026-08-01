# Last updated: 1/8/2026, 5:25:48 p.m.
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        for num in range(1, 2001):
            present = False
            valid = True

            for j in range(len(fronts)):
                if fronts[j] == num:
                    fronts[j], backs[j] = backs[j], fronts[j]
                
                if backs[j] == num: present = True
                if fronts[j] == num: valid = False

            if present and valid: return num

        return 0