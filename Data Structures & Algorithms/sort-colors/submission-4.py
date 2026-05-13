class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        track = len(nums)-1
        while track > 0:
            for e in range(0,track):
                if nums[e] > nums[e+1]:
                    tmp = nums[e+1]
                    nums[e+1]=nums[e]
                    nums[e]=tmp
            track-=1

		