class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        temp = []
        for i in range(len(nums)):
            res = 1
            for j in range(i+1,len(nums)):
                res *= nums[j]
            for k in temp:
                res *= k
            out.append(res)
            temp.append(nums[i])
        
        return out