class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if r>=m or c>=n or min(r,c)<0 or grid[r][c]=="0":
                return
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count

            