class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxarea=0
        while l<r:
            maxarea=max(maxarea,(min(heights[l],heights[r])*(r-l)))
            print(l,r,maxarea)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxarea