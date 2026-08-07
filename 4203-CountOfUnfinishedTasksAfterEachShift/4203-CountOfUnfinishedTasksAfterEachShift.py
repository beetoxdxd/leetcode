# Last updated: 7/8/2026, 5:46:52 p.m.
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix = [tasks[0]]
        n = len(tasks)

        for i in range(1, n):
            prefix.append(prefix[i-1] + tasks[i])
            
        ans = []
        curr_work = 0
        total_time = prefix[-1]

        for shift in shifts:
            curr_work += shift

            if curr_work >= total_time:
                ans.append(0)
                curr_work = 0
                continue

            ans.append(n-bisect_right(prefix, curr_work))

        return ans