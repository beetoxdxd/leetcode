# Last updated: 1/8/2026, 5:26:17 p.m.
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        if n < m:
            s1, s2 = s2, s1
            n, m = m, n

        row = [0]
        for i in range(m): row.append(ord(s2[i]) + row[-1])
        
        for i in range(n):
            prev_diagonal = row[0]
            row[0] += ord(s1[i])

            for j in range(m):
                diagonal = row[j+1]
                if s1[i] == s2[j]: row[j+1] = prev_diagonal
                else: row[j+1] = min(row[j+1] + ord(s1[i]), row[j] + ord(s2[j]))

                prev_diagonal = diagonal
            
        return row[-1]