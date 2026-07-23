# Last updated: 22/7/2026, 11:36:01 p.m.
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        for i in range(31):
            if n & (1 << i): powers.append(i)

        prefix_sums = [0]
        for p in powers:
            prefix_sums.append(prefix_sums[-1] + p)

        modulo = 10**9 + 7
        ans = []

        for query in queries:
            ans.append(2**(prefix_sums[query[1]+1] - prefix_sums[query[0]]) % modulo)
            
        return ans