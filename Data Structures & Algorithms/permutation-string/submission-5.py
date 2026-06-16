class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        s1_counts = Counter(s1)
        count = {}
        for i in range(len(s2)-j+1):
            #out_char = s2[i]
            #in_char = s2[i+j]
            #count[out_char] -= 1
            #count[in_char] += 1
            window_counts = Counter(s2[i:j+i])
            if s1_counts == window_counts:
                return True
        return False