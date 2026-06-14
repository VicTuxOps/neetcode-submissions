class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        out = []
        nums = sorted(nums)
        print(nums)
        mem = set()
        for i in range(0,len(nums)-1):
            print(i)
            findN = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                target = nums[l] + nums[r]
                if findN == target and [nums[l],nums[r],nums[i]] not in out:
                    out.append([nums[l],nums[r],nums[i]])
                    r-=1
                    l+=1
                elif findN > target:
                    l+=1
                else:
                    r-=1
        
        return out