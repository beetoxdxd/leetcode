# Last updated: 22/7/2026, 11:36:03 p.m.
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_idx)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                finish_time, room = heapq.heappop(busy_rooms)
                new_end = finish_time + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))
            
            count[room] += 1
            
        return count.index(max(count))