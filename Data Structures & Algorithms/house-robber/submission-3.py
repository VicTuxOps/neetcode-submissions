class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 1:
            return 0
        
        result1 = max(nums[0],nums[1])
        result2 = nums[0]
        i = 2
        while i<= len(nums)-1:
            temp = max(result1, nums[i] + result2)
            result1, result2 = temp, result1
            i+=1
        return temp
        