# Last updated: 1/8/2026, 5:26:31 p.m.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []

        for log in logs:
            func_id, op, timestamp = log.split(':')
            if op == "start":
                stack.append(log)
            else:
                aux = stack.pop(-1)
                prev_id, prev_op, prev_time = aux.split(':')
                interval = int(timestamp) - int(prev_time) + 1
                ans[int(func_id)] += interval
                if stack != []: 
                    prev_id, prev_op, prev_time = stack[-1].split(':')
                    ans[int(prev_id)] -= interval
            
        return ans