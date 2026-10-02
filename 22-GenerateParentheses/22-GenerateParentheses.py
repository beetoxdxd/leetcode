# Last updated: 1/10/2026, 6:08:59 p.m.
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        solutions = []
4
5        def generation(num: int, balance: int, comb: str) -> None:
6            if balance < 0: return
7            if num == 0: 
8                solutions.append(comb + ')'*balance)
9                return
10            generation(num-1, balance+1, comb + '(')
11            generation(num, balance-1, comb + ')')
12            
13        generation(n, 0, '')
14        return solutions