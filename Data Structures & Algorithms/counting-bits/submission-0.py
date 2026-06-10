class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n+1):
            tmp = 0
            while i > 0:
                if i & 1 == 1:
                    tmp+=1
                i = i >> 1
            count.append(tmp)
        return count