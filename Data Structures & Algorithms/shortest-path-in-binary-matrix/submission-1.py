class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r, c = 0,0
        if grid[r][c] == 1:
            return -1
        visit = set()
        queue = deque()
        visit.add((r,c))
        queue.append((r,c))
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n-1 and c == n-1:
                    return length
                neighbors = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
                for dr, dc in neighbors:
                    newr = r+dr
                    newc = c+dc
                    if (min(newr,newc)<0 or newr >= n or newc >= n or (newr,newc) in visit or grid[newr][newc]==1):
                        continue
                    visit.add((newr,newc))
                    queue.append((newr,newc))
            length+=1
        return -1