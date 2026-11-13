# Last updated: 12/11/2026, 10:49:35 p.m.
1class Solution:
2    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        ans = 0
5        operations = 0
6        # Maintain the window maximum with a priority queue
7        q = []
8        # Record the set of elements covered by this index
9        cnt = [[] for _ in range(n)]
10        # Index of the first greater-or-equal element to the right
11        pos = [n] * n
12        # Decreasing monotonic stack
13        st = []
14
15        left = 0
16        for right in range(n):
17            # Maintain the monotonic stack
18            while st and nums[right] >= nums[st[-1]]:
19                pos[st[-1]] = right
20                st.pop()
21            # The stack top is the nearest greater element to the left of nums[right]
22            if st:
23                cnt[st[-1]].append(right)
24            st.append(right)
25
26            # The priority queue front is the window maximum
27            heapq.heappush(q, (-nums[right], right))
28            # Adding nums[right] increases the operation count
29            operations += max(0, -q[0][0] - nums[right])
30
31            # The minimum operation count exceeds k; shrink the window
32            while operations > k:
33                # Removing nums[left] from the window decreases the operation count
34                for i in cnt[left]:
35                    # Subtract the contribution
36                    operations -= (nums[left] - nums[i]) * (
37                        min(pos[i], right + 1) - i
38                    )
39                left += 1
40
41            # Remove elements with indices less than left from the priority queue
42            while q and q[0][1] < left:
43                heapq.heappop(q)
44
45            # There are right - left + 1 valid contiguous subarrays ending at right
46            ans += right - left + 1
47
48        return ans