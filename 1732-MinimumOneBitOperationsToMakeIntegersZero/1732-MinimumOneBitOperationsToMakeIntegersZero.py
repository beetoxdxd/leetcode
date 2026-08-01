# Last updated: 1/8/2026, 5:23:19 p.m.
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        n >>= 1 # Desplaza los bits una posición a la derecha
        while n > 0:
            ans ^= n # XOR con los bits desplazados
            n >>= 1
        return ans