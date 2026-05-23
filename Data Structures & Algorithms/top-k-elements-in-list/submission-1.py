class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0)+1
        
        i = 0
        for j in sorted(counts):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1

        top_k = heapq.nlargest(k, counts.items(), key=lambda x: x[1])
        result = [item[0] for item in top_k]
        return result
                