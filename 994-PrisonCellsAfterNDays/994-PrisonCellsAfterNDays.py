# Last updated: 1/8/2026, 5:25:20 p.m.
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        diff = []
        for i in range(14):
            aux = cells[:]
            for j in range(1, 7):
                if (cells[j-1] == 1 and cells[j+1] == 1) or (cells[j-1] == 0 and cells[j+1] == 0):
                    aux[j] = 1
                else: aux[j] = 0
            
            aux[0] = 0
            aux[7] = 0
            cells = aux
            diff.append(aux)
            
        return diff[(n-1)%14]