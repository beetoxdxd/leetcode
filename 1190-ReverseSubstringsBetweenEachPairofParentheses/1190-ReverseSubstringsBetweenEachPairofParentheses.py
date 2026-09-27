# Last updated: 27/9/2026, 5:53:28 p.m.
1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        open_parentheses_indices = deque()
4        result = []
5
6        for current_char in s:
7            if current_char == "(":
8                # Store the current length as the start index
9                # for future reversal
10                open_parentheses_indices.append(len(result))
11            elif current_char == ")":
12                start = open_parentheses_indices.pop()
13                # Reverse the substring between the matching parentheses
14                result[start:] = result[start:][::-1]
15            else:
16                # Append non-parenthesis characters to the processed list
17                result.append(current_char)
18        return "".join(result)