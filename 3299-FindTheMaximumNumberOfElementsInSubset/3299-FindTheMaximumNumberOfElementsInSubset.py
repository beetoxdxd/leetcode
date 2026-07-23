# Last updated: 22/7/2026, 11:35:27 p.m.
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        h = Counter(nums)
        ans = 1

        for key, value in h.items():
            if value == 1: continue
            if key == 1: 
                aux = value if value % 2 else value-1
                ans = max(ans, aux)
                continue

            # hay al menos dos valores, se puede cumplir la condicion
            exp = key**2
            cont = 1
            
            while exp in h: 
                cont += 2

                if h[exp] == 1: break
                exp **=2

            ans = max(ans, cont)

        return ans