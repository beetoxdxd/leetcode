# Last updated: 1/8/2026, 5:24:22 p.m.
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {start}
        queue = deque([start])
        n = len(arr)

        while queue:
            current = queue.popleft()
            if arr[current] == 0: return True
            i, j = current + arr[current], current - arr[current]
            if i >= 0 and i < n and i not in visited: queue.append(i)
            if j >= 0 and j < n and j not in visited: queue.append(j)

            visited.add(current)

        return False