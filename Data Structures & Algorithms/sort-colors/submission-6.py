class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = len(nums) - 1
        track = 0
        while track <= blue:
            if nums[track] == 0:
                nums[red], nums[track] = nums[track], nums[red]
                track+=1
                red+=1
            elif nums[track] == 2:
                nums[blue], nums[track] = nums[track], nums[blue]
                blue-=1
            else:
                track+=1