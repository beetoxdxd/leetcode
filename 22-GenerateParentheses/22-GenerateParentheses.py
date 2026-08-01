# Last updated: 1/8/2026, 5:29:07 p.m.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []

        def generation(num: int, balance: int, comb: str) -> None:
            if balance < 0: return
            if num == 0: 
                solutions.append(comb + ')'*balance)
                return
            generation(num-1, balance+1, comb + '(')
            generation(num, balance-1, comb + ')')
            
        generation(n, 0, '')
        return solutions