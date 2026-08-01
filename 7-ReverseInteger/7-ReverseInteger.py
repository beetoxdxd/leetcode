# Last updated: 1/8/2026, 5:29:34 p.m.
class Solution:
    def reverse(self, x: int) -> int:
        limit = str(1 << 31)
        number = ""
        aux = str(x)
        start = 0 if aux[0] == '-' else -1
        for digit in range(len(aux)-1, start, -1):
            number += aux[digit]

        if len(number) > len(limit): return 0
        if len(number) < len(limit): return int(number)*-1 if aux[0] == '-' else int(number)
        #print("Limite: ", limit)
        #print("Numero: ", number)
        for i in range(len(number)):
            if number[i] > limit[i]: return 0
            elif number[i] < limit[i]: break

        return int(number)*-1 if aux[0] == '-' else int(number)
