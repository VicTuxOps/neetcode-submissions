from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.sink(nums, i, n)

        # Repeatedly move max to the end
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.sink(nums, 0, end)

        return nums

    def sink(self, nums: List[int], i: int, heap_size: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < heap_size and nums[left] > nums[largest]:
                largest = left

            if right < heap_size and nums[right] > nums[largest]:
                largest = right

            if largest == i:
                break

            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest