# Last updated: 22/7/2026, 11:36:22 p.m.
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        l = len(tickets)

        while tickets:
            if tickets[0] == 1 and k == 0: break
            aux = tickets.pop(0) - 1
            if aux: tickets.append(aux)
            else: l -= 1

            k = (k-1) % l
            ans += 1        

        return ans + 1