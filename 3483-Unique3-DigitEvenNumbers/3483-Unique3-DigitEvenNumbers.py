# Last updated: 10/9/2026, 10:29:34 p.m.
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        even_numbers = set()
4        n = len(digits)
5
6
7        def traverse(num: int, index: list) -> None:
8            if len(str(num)) == 3: 
9                if num % 2 == 0: even_numbers.add(num)
10                return
11
12            for i in range(n):
13                if i in index: continue
14                traverse(num*10 + digits[i], index + [i])
15
16        traverse(0, [])
17        return len(even_numbers)