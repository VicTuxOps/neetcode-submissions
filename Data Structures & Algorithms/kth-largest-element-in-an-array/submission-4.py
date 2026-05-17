class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for val in nums:
            heapq.heappush(min_heap, val)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]