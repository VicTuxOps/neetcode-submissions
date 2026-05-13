class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.limit = maxNumbers
        self.next_val = 0
        self.available = set()

    def get(self) -> int:
        if self.available:
            return self.available.pop()
        if self.next_val < self.limit:
            val = self.next_val
            self.next_val += 1
            return val
        return -1

    def check(self, number: int) -> bool:
        if number < 0 or number >= self.limit:
            return False
        return number in self.available or (number >= self.next_val and number <= self.limit-1)

    def release(self, number: int) -> None:
        if number < self.next_val and number not in self.available:
            self.available.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
