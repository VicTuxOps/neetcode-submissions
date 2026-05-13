class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        start = 0 #index of list

        def backtrack(start, path, target):
            reach = False
            if target == 0:
                reach = True
            elif target < 0:
                return
            elif nums[start] > target:
                start+=1
            if reach and sorted(path) not in res:
                res.append(sorted(path[:]))
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, target - nums[i])
                path.pop()
        backtrack(0, [], target)
        return res