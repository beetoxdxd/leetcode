# Last updated: 1/8/2026, 5:25:29 p.m.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = [fruits[0]]
        n = len(fruits)
        i = 0
        start = 0
        ans = 0

        while i < n:
            if fruits[i] == basket[0]: 
                i+=1
                ans += 1
                continue
            basket.append(fruits[i])
            aux = i
            while i < n and fruits[i] in basket: 
                if fruits[aux] != fruits[i]: aux = i
                i += 1
                
            ans = max(ans, i - start)
            start = aux
            if fruits[start] == basket[0]: basket.pop(1)
            else: basket.pop(0)
            

        return ans