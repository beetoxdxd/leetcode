# Last updated: 22/7/2026, 11:36:13 p.m.
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        maxasteroid = max(asteroids)
        freq = [0] * (maxasteroid + 1)
        
        for a in asteroids:
            freq[a] += 1
            
        currentmass = mass
        for i in range(1, maxasteroid + 1):
            if freq[i] > 0:
                if i > currentmass:
                    return False
                currentmass += i * freq[i]
                
        return True