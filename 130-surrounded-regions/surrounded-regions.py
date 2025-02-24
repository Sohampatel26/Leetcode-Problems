class Solution:
    def solve(self, board: List[List[str]]) -> None:
       
        m=len(board)
        n=len(board[0])

        if not board:
            return None
        
        def dfs(r,c):
            if r>=m or c>=n or min(r,c)<0 or board[r][c]!='O':
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for c in range(n):
            if board[0][c]=='O':
                dfs(0,c)
            if board[m-1][c]=='O':
                dfs(m-1,c)
        
        for r in range(m):
            if board[r][0]=='O':
                dfs(r,0)
            if board[r][n-1]=='O':
                dfs(r,n-1)

        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
       
        for r in range(m):
            for c in range(n):
                if board[r][c]=='T':
                    board[r][c]='O'
        

