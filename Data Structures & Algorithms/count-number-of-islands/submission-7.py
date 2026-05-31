class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    count+=1
        return count

    def dfs(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])
        if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return None
        grid[r][c] = "0"
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for dr, dc in directions:
            newr, newc = r + dr, c + dc
            self.dfs(grid, newr, newc)
        return None