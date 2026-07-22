# Last updated: 22/7/2026, 5:57:21 p.m.
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        occurrences = {}
        for i in range(k):
            if nums[i] in occurrences: occurrences[nums[i]] += 1
            else: occurrences[nums[i]] = 1

        
        ans = []
        start = 0
        size = len(nums)
        m = max(list(occurrences.values()))
        for i in range(k, size+1):
            pq = []
            for key in occurrences:
                heapq.heappush(pq, (m-occurrences[key], key))

            j = 0
            sub = 0
            while pq and j < x:
                priority, value = heapq.heappop(pq)
                values = [value]
                while pq:
                    aux, aux2 = heapq.heappop(pq)
                    if aux == priority: values.append(aux2)
                    else:
                        heapq.heappush(pq, (aux, aux2))
                        break
                while values and j < x:
                    sub += values.pop() * (priority-m) * -1
                    j += 1

            ans.append(sub)
            occurrences[nums[start]] -= 1
            if occurrences[nums[start]] == m-1: m = max(list(occurrences.values()))
            if occurrences[nums[start]] == 0: del occurrences[nums[start]]
            if i != size:
                if nums[i] in occurrences: occurrences[nums[i]] += 1
                else: occurrences[nums[i]] = 1

                if occurrences[nums[i]] > m: m = occurrences[nums[i]]

            
            start += 1        

        return ans
