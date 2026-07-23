# Last updated: 22/7/2026, 11:35:58 p.m.
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        lowest = penalty
        hour = 0

        for i, customer in enumerate(customers):
            if customer == 'Y': penalty -= 1
            else: penalty += 1
        
            if lowest > penalty:
                lowest = penalty
                hour = i+1

        return hour