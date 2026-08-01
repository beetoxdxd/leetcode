# Last updated: 1/8/2026, 5:23:16 p.m.
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        h = {piece[0]: piece for piece in pieces}

        i = 0
        n = len(arr)
        while i < n:
            if arr[i] not in h: return False
            
            piece = h[arr[i]]
            j, m = 0, len(piece)
            while i < n and j < m and arr[i] == piece[j]: i += 1; j += 1
            if j != m: return False

        return True