class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map_row =  defaultdict(set)
        map_column =  defaultdict(set)
        map_square =  defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                element = board[row][col]
                if element != ".":
                    square_idx = (row//3) * 3 + (col//3)
                    if element not in map_row[row]:
                        map_row[row].add(element)
                    else:
                        return False
                    if element not in map_column[col]:
                        map_column[col].add(element)
                    else:
                        return False
                    if element not in map_square[square_idx]:
                        map_square[square_idx].add(element)
                    else:
                        return False
        return True
                

