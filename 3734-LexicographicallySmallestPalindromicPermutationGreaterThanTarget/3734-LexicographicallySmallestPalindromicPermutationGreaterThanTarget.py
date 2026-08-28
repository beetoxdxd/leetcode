# Last updated: 27/8/2026, 10:23:21 p.m.
1class Solution:
2    def lexPalindromicPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4        # Special case: length of 1
5        if n == 1:
6            return s if s > target else ""
7
8        # Count the frequency of each character
9        cnt = [0] * 26
10        for c in s:
11            cnt[ord(c) - ord("a")] += 1
12
13        # Check if it can form a palindrome and record the characters with odd occurrences
14        odd_char = ""
15        for i in range(26):
16            if cnt[i] % 2 == 1:
17                # More than one character appears an odd number of times, cannot form a palindrome
18                if odd_char != "":
19                    return ""
20                odd_char = chr(ord("a") + i)
21            cnt[
22                i
23            ] //= 2  # It takes only half the characters to construct the left half
24
25        prefix = []
26
27        def check(c):
28            left = prefix.copy()
29            left.append(c)
30            for i in range(25, -1, -1):
31                left.extend([chr(ord("a") + i)] * cnt[i])
32
33            palindrome = left + [odd_char] + left[::-1]
34
35            return "".join(palindrome) > target
36
37        # Construct the left part of each digit greedily
38        for i in range(n // 2):
39            found = False
40            # Try to place the smallest character in lexicographical order
41            for j in range(26):
42                if cnt[j] == 0:
43                    continue
44
45                cnt[j] -= 1
46                if check(chr(ord("a") + j)):
47                    # If the constructed palindrome is greater than target, choose the character
48                    prefix.append(chr(ord("a") + j))
49                    found = True
50                    break
51                else:
52                    cnt[j] += 1  # Not meeting the conditions, reset the counter
53            if not found:
54                return ""  # Cannot construct a palindrome larger than target
55
56            if prefix[i] > target[i]:  # prefix is already greater than target
57                left = prefix[:]
58                for j in range(26):
59                    left.extend([chr(ord("a") + j)] * cnt[j])
60                palindrome = left + [odd_char] + left[::-1]
61                return "".join(palindrome)
62
63        # Construct the final palindrome string
64        ans = prefix + [odd_char] + prefix[::-1]
65        return "".join(ans)