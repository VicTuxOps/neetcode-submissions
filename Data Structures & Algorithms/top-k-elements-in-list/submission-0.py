class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n,0)+1
        
        out = sorted(counts, key=counts.get, reverse=True)

        return out[:k]
                