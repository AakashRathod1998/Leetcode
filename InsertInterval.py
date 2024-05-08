class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        for i in intervals:
            if not stack or stack[-1][1] < i[0]:
                stack.append(i)
            else:
                stack[-1][1] = max(stack[-1][1],i[1])

        return stack
