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
                tmp = nums[red]
                nums[red] = nums[track]
                nums[track] = tmp
                track+=1
                red+=1
            elif nums[track] == 2:
                tmp = nums[blue]
                nums[blue] = nums[track]
                nums[track] = tmp
                blue-=1
            else:
                track+=1