# Last updated: 22/7/2026, 11:36:00 p.m.
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        n = len(queries[0])
        
        for query in queries:
            for word in dictionary:
                edits = 0
                
                for i in range(n):
                    if edits > 2: break
                    if query[i] != word[i]: edits += 1

                if edits <= 2: 
                    ans.append(query)
                    break

        return ans