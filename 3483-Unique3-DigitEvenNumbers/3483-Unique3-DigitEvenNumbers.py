# Last updated: 10/9/2026, 11:06:25 p.m.
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        javob=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i==k or i==j or k==j:
                        continue

                    if digits[i]==0:
                        continue

                    if digits[k]%2!=0:
                        continue

                    son=digits[i]*100 +digits[j]*10 +digits[k]
                    javob.add(son)
        return len(javob)