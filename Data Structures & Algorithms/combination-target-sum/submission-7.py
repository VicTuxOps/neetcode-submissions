class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        start = 0 #index of list

        def backtrack(start, path, target):
            if target == 0:
                res.append(sorted(path[:]))
            elif target < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, target - nums[i])
                path.pop()
        backtrack(0, [], target)
        return res