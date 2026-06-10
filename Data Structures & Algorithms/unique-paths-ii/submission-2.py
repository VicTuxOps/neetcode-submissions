class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
             return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        prevPath = [0]*cols
        prevPath[cols-1] = 1
        for r in range(rows-1,-1,-1):
            currPath = [0]*cols

            for c in range(cols-1,-1,-1):
                if obstacleGrid[r][c]:
                    currPath[c] = 0
                else:
                    if c < cols - 1:
                        currPath[c] = currPath[c+1] + prevPath[c]
                    else:
                        currPath[c] = prevPath[c]
            prevPath = currPath
        
        return prevPath[0]