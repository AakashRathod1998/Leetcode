class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        rooms, count = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1
            rooms = max(rooms,count)

        return rooms
        
        # if not intervals:
        #     return 0
        # intervals.sort(key=lambda x: x[0])
        # min_heap = []
        # heapq.heappush(min_heap, intervals[0][1])

        # for i in intervals[1:]:
        #     if min_heap[0] <= i[0]:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, i[1])
        # return len(min_heap)
