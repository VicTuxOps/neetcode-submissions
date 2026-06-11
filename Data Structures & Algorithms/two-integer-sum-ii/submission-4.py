class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < len(numbers) or j > 0:
            p1 = numbers[i]
            p2 = numbers[j]
            if p1 + p2 == target:
                return [i+1,j+1]
            elif p1 + p2 > target:
                j -=1
            else:
                i+=1
        return [0,0]