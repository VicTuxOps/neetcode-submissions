class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)+1
        cols = len(text2)+1
        out = [[0]*cols for _ in range(rows)]
        
        for r in range(rows-2,-1,-1):
            for c in range(cols-2,-1,-1):
                if text1[r] == text2[c]:
                    out[r][c] = 1 + out[r+1][c+1]
                else:
                    out[r][c] = max(out[r+1][c], out[r][c+1])
        
        return out[0][0]