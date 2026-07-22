# Last updated: 22/7/2026, 5:57:00 p.m.
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        window_size = 0
        ans = 0
        count_ones = 0

        i, n = 0, len(s)
        while i < n and s[i] == '1': i += 1
        while i < n and s[i] == '0': i += 1; window_size += 1        
        while i < n and s[i] == '1': i += 1; window_size += 1; count_ones += 1
        if i == n: return total_ones

        while True:
            if i >= n: break
            aux = 0

            while i < n and s[i] == '0':
                window_size += 1
                aux += 1
                i += 1
            
            ans = max(ans, window_size + total_ones - count_ones)
            window_size = aux
            count_ones = 0

            while i < n and s[i] == '1':
                window_size += 1
                i += 1
                count_ones += 1

        return ans