class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prefix_products = [1] * len(nums)
        running_product = 1
        right_product = 1
        for i in range(len(nums)):
            prefix_products[i] = running_product
            running_product *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            prefix_products[i] *= right_product
            right_product *= nums[i]
        return prefix_products