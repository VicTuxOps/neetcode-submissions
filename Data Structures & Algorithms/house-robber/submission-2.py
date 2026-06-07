class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 1:
            return 0
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        i = 2
        while i<= len(nums)-1:
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            i+=1
        return dp[-1]
        