class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0, 1
        maxN = 1
        out = 1
        known = set()
        known.add(s[i])
        while j < len(s):
            if s[j] not in known:
                known.add(s[j])
                out = j - i + 1
                j+=1
            else:
                while s[j] in known:
                    known.remove(s[i])
                    i+=1
            if out > maxN:
                maxN = out
        
        return maxN