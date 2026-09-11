# Last updated: 10/9/2026, 10:31:15 p.m.
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        even_numbers = set()
4        n = len(digits)
5
6        def traverse(num: int, index: list) -> None:
7            if len(str(num)) == 3: 
8                if num % 2 == 0: even_numbers.add(num)
9                return
10
11            for i in range(n):
12                if i in index: continue
13                traverse(num*10 + digits[i], index + [i])
14
15        traverse(0, [])
16        return len(even_numbers)