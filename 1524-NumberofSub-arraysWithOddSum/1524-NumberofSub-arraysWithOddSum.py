# Last updated: 14/11/2026, 11:48:59 p.m.
1class Solution:
2    def numOfSubarrays(self, arr: List[int]) -> int:
3        MOD = 10**9 + 7
4        count = prefix_sum = 0
5        # even_count starts as 1 since the initial sum (0) is even
6        odd_count = 0
7        even_count = 1
8
9        for num in arr:
10            prefix_sum += num
11            # If current prefix sum is even, add the number of odd subarrays
12            if prefix_sum % 2 == 0:
13                count += odd_count
14                even_count += 1
15            else:
16                # If current prefix sum is odd, add the number of even
17                # subarrays
18                count += even_count
19                odd_count += 1
20
21            count %= MOD  # To handle large results
22
23        return count