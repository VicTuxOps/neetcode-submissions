class Solution:
    def is_number(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False
    
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            match s:
                case str() as s if self.is_number(s):
                    stack.append(int(s))
                case "+":
                    stack.append(stack[-2] + stack[-1])
                case "D":
                    stack.append(stack[-1] * 2)
                case "C":
                    stack.pop()
            print(stack)
        
        return sum(stack)