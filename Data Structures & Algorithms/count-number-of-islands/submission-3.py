class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = 0,0
        visit = set()
        count = 0
        while r < len(grid):
            while c < len(grid[0]):
                if grid[r][c] == "1" and (r,c) not in visit:
                    count+=self.dfs(grid, r, c, visit)
                    visit.add((r,c))
                c+=1
            c = 0
            r+=1
        return count

    def dfs(self, grid, r, c, visit):
        rows, cols = len(grid), len(grid[0])
        if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == "0":
            return 0
        visit.add((r,c))
        self.dfs(grid, r+1, c, visit)
        self.dfs(grid, r-1, c, visit)
        self.dfs(grid, r, c+1, visit)
        self.dfs(grid, r, c-1, visit)
        return 1