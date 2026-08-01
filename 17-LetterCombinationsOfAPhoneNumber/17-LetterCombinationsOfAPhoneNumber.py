# Last updated: 1/8/2026, 5:29:16 p.m.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def traverse(i: int) -> List[str]:
            if i >= len(digits): return ['']

            index_comb = int(digits[i])-2
            comb = []
            for letter in combinations[index_comb]:
                for t in traverse(i+1):
                    comb.append(letter + t)
            
            return comb

        return traverse(0)