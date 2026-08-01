# Last updated: 1/8/2026, 5:27:45 p.m.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        
        prev = [1]
        for i in range(rowIndex+1):
            row = [1]
            for j in range(1, i): row.append(prev[j] + prev[j-1])
            row.append(1)
            prev = row[:]
            row.clear()
        return prev