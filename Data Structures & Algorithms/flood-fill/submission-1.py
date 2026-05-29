class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        startPixel = image[sr][sc]
        visit = set()
        image = self.dfs(image, ROWS, COLS, sr, sc, startPixel, color, visit)

        return image
    
    def dfs(self, image, ROWS, COLS, sr, sc, initColor, color, visit):
        if min(sr, sc) < 0 or sr > ROWS - 1 or sc > COLS - 1 or (sr,sc) in visit or image[sr][sc] != initColor:
            return image
        elif image[sr][sc] == initColor:
            image[sr][sc] = color
                
        visit.add((sr,sc))
        image = self.dfs(image, ROWS, COLS, sr + 1, sc, initColor, color, visit)
        image = self.dfs(image, ROWS, COLS, sr - 1, sc, initColor, color, visit)
        image = self.dfs(image, ROWS, COLS, sr, sc + 1, initColor, color, visit)
        image = self.dfs(image, ROWS, COLS, sr, sc - 1, initColor, color, visit)
        return image