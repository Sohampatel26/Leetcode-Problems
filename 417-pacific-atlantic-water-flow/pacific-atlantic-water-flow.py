class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic=set()
        pacific=set()
        m=len(heights)
        n=len(heights[0])

        def dfs(r,c,visited,height):
            if r>=m or c>=n or min(r,c)<0 or heights[r][c]<height or (r,c) in visited:
                return
            
            visited.add((r,c))


            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for c in range(n):
            dfs(0,c,pacific,heights[0][c])
            dfs(m-1,c,atlantic,heights[m-1][c])
        
        for r in range(m):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,n-1,atlantic,heights[r][n-1])

        return list(atlantic & pacific)
