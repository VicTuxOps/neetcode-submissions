class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #nums.append(nums[0])

        self.heap = [None] + nums
        res = []
        cur = (len(self.heap)-1)//2
        while cur > 0:
            i = cur
            while 2*i < len(self.heap):
                if (2*i+1 < len(self.heap) and (self.heap[2*i+1] < self.heap[2*i]) and (self.heap[i] > self.heap[2*i+1])):
                    self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                    i = 2*i+1
                elif self.heap[2*i] < self.heap[i]:
                    self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                    i = 2*i
                else:
                    break
            cur -=1
        
        while len(self.heap) > 1:
            res.append(self.pop())
        return res
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and (self.heap[2*i+1] < self.heap[2*i]) and (self.heap[i] > self.heap[2*i+1])):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1
            elif self.heap[2*i] < self.heap[i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break
        return res