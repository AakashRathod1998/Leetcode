class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        stack = []

        for i in intervals:
            if not stack or stack[-1][1] <= i[0]:
                stack.append(i)
            else:
                return False
        return len(intervals) == len(stack)
