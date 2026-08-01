# Last updated: 1/8/2026, 5:25:36 p.m.
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        possibles = {"011237","0122579","012356789","0124","0134449", "0145678","01466788","0248","0368888","0469","1","112234778","11266777","122446","125","128","1289","13468","16","2","224588","23","23334455","234455668","23678","256","35566","4","46","8"}
        
        digits = []
        while n > 0:
            digits.append(str(n%10))
            n //= 10
        
        digits.sort()
        if "".join(digits) in possibles: return True

        return False