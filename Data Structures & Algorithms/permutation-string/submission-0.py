class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        for i in range(len(s2)):
            if sorted(s2[i:j]) == sorted(s1):
                return True
            j+=1
        return False