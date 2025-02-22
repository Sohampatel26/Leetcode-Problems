from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"  # Mark as visited

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":  # Found a new island
                    count += 1
                    bfs(r, c)  # Explore using BFS

        return count
