from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda s:s[0])
        prevend=intervals[0][1]
        removals=0

        for i in intervals[1:]:
            if i[0]>=prevend:
                prevend=i[1]
            
            else:
                removals+=1
                prevend=min(prevend,i[1])
        return removals



