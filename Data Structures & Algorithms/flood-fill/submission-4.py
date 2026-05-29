class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS = len(image)
        COLS = len(image[0])
        startPixel = image[sr][sc]
        image = self.dfs(image, ROWS, COLS, sr, sc, startPixel, color)

        return image
    
    def dfs(self, image, ROWS, COLS, sr, sc, initColor, color):
        if min(sr, sc) < 0 or sr > ROWS - 1 or sc > COLS - 1 or image[sr][sc] != initColor:
            return
        elif image[sr][sc] == initColor:
            image[sr][sc] = color

        self.dfs(image, ROWS, COLS, sr + 1, sc, initColor, color)
        self.dfs(image, ROWS, COLS, sr - 1, sc, initColor, color)
        self.dfs(image, ROWS, COLS, sr, sc + 1, initColor, color)
        self.dfs(image, ROWS, COLS, sr, sc - 1, initColor, color)
        return image