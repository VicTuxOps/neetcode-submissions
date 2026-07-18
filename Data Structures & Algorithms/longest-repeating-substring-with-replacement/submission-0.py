class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sizeS = len(s)
        cntDict = defaultdict(int)
        max_freq, out = 0, 0
        l = 0
        for r in range(sizeS):
            char = s[r]
            cntDict[char] += 1
            max_freq = max(max_freq, cntDict[char])
            window_length = r - l + 1
            while window_length - max_freq > k:
                new_char = s[l]
                cntDict[new_char]-=1
                l+=1
                window_length = r - l + 1
            
            out = max(out, window_length)
        
        return out