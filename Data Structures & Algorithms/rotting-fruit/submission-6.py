class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        minutes = 0
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in neighbors:
                    newr = r + dr
                    newc = c + dc
                    if (min(newr,newc) < 0 or newr == ROWS or newc == COLS or (newr,newc) in visit or grid[newr][newc] == 0):
                        continue
                    elif grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        fresh-=1
                        queue.append((newr,newc))
                    visit.add((newr,newc))
                    
            if queue:
                minutes += 1
        
        if fresh > 0:
            return -1
        return minutes