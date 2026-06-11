class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        while i < len(numbers):
            p1 = numbers[i]
            p2 = numbers[j]
            if p1 + p2 == target:
                return [i+1,j+1]
            if j >= len(numbers)-1:
                i+=1
                j = i + 1
            else:
                j += 1
        
        return [0,0]