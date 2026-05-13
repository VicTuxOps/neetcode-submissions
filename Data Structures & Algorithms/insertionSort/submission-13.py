# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sizeP = len(pairs)
        if sizeP == 0:
            return []
        out = [pairs.copy()]
        for i in range(1, sizeP):
            curr = i
            while curr > 0 and (pairs[curr - 1].key > pairs[curr].key):
                pairs[curr - 1], pairs[curr] = pairs[curr], pairs[curr - 1]
                curr -= 1
            out.append(pairs.copy())

        return out