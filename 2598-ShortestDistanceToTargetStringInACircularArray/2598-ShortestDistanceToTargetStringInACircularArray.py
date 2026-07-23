# Last updated: 22/7/2026, 11:35:55 p.m.
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: return 0
        
        n = len(words)
        i = (startIndex + 1) % n
        j = (startIndex - 1 + n) % n
        cont = 1

        while i != startIndex and j != startIndex:
            if words[i] == target or words[j] == target: return cont

            i = (i + 1) % n
            j = (j - 1 + n) % n
            cont += 1

        return -1