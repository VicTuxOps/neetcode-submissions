class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        i, j = 0, 0
        temp = {j}
        res = 1
        while j < len(nums):
            if i not in temp:
                res *= nums[i]
            if i == len(nums)-1:
                i = 0
                j += 1
                temp.pop()
                temp.add(j)
                out.append(res)
                res = 1
            else:
                i+=1
        return out