# Last updated: 1/8/2026, 5:26:29 p.m.
class Solution:
    def solveEquation(self, equation: str) -> str:
        num_x = [0,0]
        sides = [0,0]
        s = 0
        i = 0
        n = len(equation)
        sign = '+'

        while i < n:
            if equation[i] == '=': 
                s = 1
                sign = '+'
            elif equation[i] == '+' or equation[i] == '-': sign = equation[i]
            elif equation[i] == 'x': 
                if sign == '+': num_x[s] += 1
                else: num_x[s] -= 1
            else: # numero
                num = 0
                while i < n and equation[i] >= '0' and equation[i] <= '9':
                    num = num*10 + int(equation[i])
                    i += 1

                if i < n and equation[i] == 'x':
                    if sign == '+': num_x[s] += num
                    else: num_x[s] -= num
                else:
                    if sign == '+': sides[s] += num
                    else: sides[s] -= num
                    continue

            i += 1

        if num_x[0] == num_x[1] and sides[0] == sides[1]: return "Infinite solutions"
        if num_x[0] == num_x[1] and sides[0] != sides[1]: return "No solution"
        
        x = num_x[0] - num_x[1]
        var = sides[1] - sides[0]
        return f"x={var//x}"