class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevend=intervals[0][1]
        lis=[intervals[0]]

        for i in intervals[1:]:
            if i[0]> prevend:
                prevend=i[1]
                lis.append(i)
            
            else:
                lis[-1][1]=max(prevend,i[1])
                prevend=max(prevend,i[1])

        return lis
        