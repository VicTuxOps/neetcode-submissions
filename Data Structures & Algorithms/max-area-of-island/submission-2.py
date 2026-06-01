class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    tmp = self.dfs(grid, visit, r, c, ROWS, COLS)
                    count = max(count,tmp)
        return count
    
    def dfs(self, grid, visit, r, c, ROWS, COLS):
        if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0):
            return 0
        visit.add((r,c))
        count = 1
        count += self.dfs(grid,visit,r+1,c, ROWS, COLS)
        count += self.dfs(grid,visit,r-1,c, ROWS, COLS)
        count += self.dfs(grid,visit,r,c+1, ROWS, COLS)
        count += self.dfs(grid,visit,r,c-1, ROWS, COLS)
        #visit.remove((r,c))
        return count