# Last updated: 1/8/2026, 5:23:37 p.m.
from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0

        cont = target[0]  # El primer valor siempre requiere ese número de operaciones
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                cont += target[i] - target[i - 1]

        return cont
