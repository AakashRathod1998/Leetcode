class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.opr = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        self.opr.append(['add'])
        self.intervals.append([left,right])

    def count(self) -> int:

        if self.opr and self.opr[-1] == 'count':
            self.opr.append(['count'])
            return self.cnt
    
        self.opr.append(['count'])
        self.cnt = 0

        self.intervals.sort(key = lambda x: (x[0],x[1]))
        merged =[]
        for i in self.intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        intervals = merged
        
        self.cnt = 0

        for i,(left, right) in enumerate(intervals):
            self.cnt += right - left + 1
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
