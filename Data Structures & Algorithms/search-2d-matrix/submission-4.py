class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target <= m[-1]:
                for n in m:
                    if target == n:
                        return True

        return False