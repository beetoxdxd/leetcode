# Last updated: 24/10/2026, 12:39:01 p.m.
1class Solution:
2    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
3        
4        max_arrive = max(arriveAlice, arriveBob)
5        min_leave = min(leaveAlice, leaveBob)
6
7        if min_leave < max_arrive: return 0
8
9        months = {
10            0: 0,
11            1: 31,
12            2: 28,
13            3: 31,
14            4: 30,
15            5: 31,
16            6: 30,
17            7: 31,
18            8: 31,
19            9: 30,
20            10: 31,
21            11: 30,
22            12: 31
23        }
24
25        month = 0
26        for i in range(int(max_arrive[:2]), int(min_leave[:2])):
27            month += months[i]
28
29        days = int(min_leave[3:]) - int(max_arrive[3:]) 
30        return month + days + 1