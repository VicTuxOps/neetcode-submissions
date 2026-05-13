class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        # Swap queues
        self.queue1, self.queue2 = self.queue2, []

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.pop(0)
        return -1

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        else:
            return -1

    def empty(self) -> bool:
        if not self.queue1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()