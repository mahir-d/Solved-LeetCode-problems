​
​
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        print(intervals)
        
        for i in range(0, len(intervals) - 1):
            start, end = intervals[i][0], intervals[i][1]
            start1, end1 = intervals[i+1][0], intervals[i+1][1]
        
            if end > start1: return False
        return True
