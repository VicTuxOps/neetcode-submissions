class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(grid, r, c, visit, idx):
            if idx == len(word):
                return True
            if r >= ROWS or c >= COLS or (r,c) in visit or min(r,c) < 0 or grid[r][c] != word[idx]:
                return False
            
            visit.add((r,c))
            flag = (dfs(grid, r+1, c, visit, idx+1) or dfs(grid, r-1, c, visit, idx+1) or dfs(grid, r, c+1, visit, idx+1) or dfs(grid, r, c-1, visit, idx+1))
            visit.remove((r,c))
            
            return flag

        myvisit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(board, r, c, myvisit, 0):
                    return True

        return False