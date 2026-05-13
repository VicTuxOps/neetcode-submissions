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
                case "+":
                    stack.append(stack[-2]+stack[-1])
                case "D":
                    tmp = stack[-1]*2
                    stack.append(tmp)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(s))
            print(stack)
        
        return sum(stack)