class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                element = board[row][col]
                if element != ".":
                    markers = [(row, element), (element, col), (row // 3, col // 3, element)]
                    if any(m in seen for m in markers):
                        return False
                    seen.update(markers)
        return True
                

