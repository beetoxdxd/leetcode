# Last updated: 1/8/2026, 5:24:16 p.m.
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        h = defaultdict(list)
        visited = set()
        queue = deque()
        n = len(arr)

        for i, num in enumerate(arr):
            h[num].append(i)

        ans = 0
        visited.add(0)
        queue.append(0)

        while queue:
            level = len(queue)

            for k in range(level):
                i = queue.popleft()
                if i == n-1: return ans
                
                if i+1 < n and i+1 not in visited: visited.add(i+1); queue.append(i+1)
                if i-1 >= 0 and i-1 not in visited: visited.add(i-1); queue.append(i-1)

                for j in h[arr[i]]:
                    if j not in visited: visited.add(j); queue.append(j)

                del h[arr[i]]

            ans += 1


        return 0