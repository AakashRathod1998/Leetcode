class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])

        for i in intervals[1:]:
            if min_heap[0] <= i[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i[1])
        return len(min_heap)
