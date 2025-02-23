class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m=len(grid)
        n=len(grid[0])
        fc=0
        minu=0
        dir=[[1,0],[0,1],[-1,0],[0,-1]]

        queue=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fc+=1
        
        while queue:
            r,c,minu=queue.popleft()
            for dr,dc in dir:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    fc-=1
                    grid[nr][nc]=2
                    queue.append((nr,nc,minu+1))
        
        return minu if fc==0 else -1

                