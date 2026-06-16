class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        maxN = 0
        known = set()
        for j in range(len(s)):
            while s[j] in known:
                known.remove(s[i])
                i+=1
            known.add(s[j])
            maxN = max(maxN, j - i + 1)
        
        return maxN