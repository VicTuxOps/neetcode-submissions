class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []
        for n in nums:
            counts[n] = counts.get(n,0)+1
        
        i = 0
        for j in sorted(counts):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for val, count in counts.items():
            freq_buckets[count].append(val)

        for i in range(len(freq_buckets) - 1, 0, -1):
            for val in freq_buckets[i]:
                result.append(val)
                if len(result) == k:
                    return result